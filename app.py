import streamlit as st
import pandas as pd
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium
import streamlit.components.v1 as components
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Delhi Danger Zones", layout="wide")
st.title("🚨 Delhi Road Accident Danger Map")

#Auto detect user location from browser
components.html("""
<script>
navigator.geolocation.getCurrentPosition(
    function(position) {
        const lat = position.coords.latitude;
        const lon = position.coords.longitude;
        const url = new URL(window.location);
        url.searchParams.set("lat", lat);
        url.searchParams.set("lon", lon);
        window.location = url;
    }
);
</script>
""", height=0)

#Load data
df = pd.read_csv("delhi_hotspot_clusters.csv")

# Clean district names
df['DISTRICT'] = df['DISTRICT'].str.upper()
df['DISTRICT'] = df['DISTRICT'].str.replace(r"\(.*\)", "", regex=True).str.strip()

# District coordinates
district_coords = {
    "CENTRAL DELHI": (28.6519, 77.2315),
    "EAST DELHI": (28.6415, 77.2946),
    "NEW DELHI": (28.6139, 77.2090),
    "NORTH DELHI": (28.7041, 77.1025),
    "NORTH EAST DELHI": (28.6863, 77.2625),
    "NORTH WEST DELHI": (28.7480, 77.0565),
    "SOUTH DELHI": (28.5244, 77.1855),
    "SOUTH EAST DELHI": (28.5300, 77.2700),
    "SOUTH WEST DELHI": (28.5733, 76.9800),
    "WEST DELHI": (28.6692, 77.0680),
    "SHAHDARA": (28.6760, 77.2890)
}

# Attach coordinates
df['LAT'] = df['DISTRICT'].map(lambda x: district_coords.get(x, (None, None))[0])
df['LON'] = df['DISTRICT'].map(lambda x: district_coords.get(x, (None, None))[1])
df = df.dropna(subset=['LAT', 'LON'])

#Get browser location
query_params = st.query_params
lat = float(query_params.get("lat", [28.6139])[0])
lon = float(query_params.get("lon", [77.2090])[0])

st.write(f"📍 Detected Location: {lat}, {lon}")

#Heatmap
delhi_map = folium.Map(location=[28.61, 77.23], zoom_start=11)
heat_data = [[r['LAT'], r['LON'], r['DANGER_SCORE']] for _, r in df.iterrows()]
HeatMap(heat_data, radius=30).add_to(delhi_map)
st_folium(delhi_map, width=1000, height=500)

#Local risk 
df['DIST'] = np.sqrt((df['LAT'] - lat)**2 + (df['LON'] - lon)**2)
radius = st.slider("Search radius (km)", 2, 15, 8)
nearby = df[df['DIST'] < (radius / 100)]
zone_risk = nearby['DANGER_SCORE'].sum()

st.subheader("📍 Live Safety Status")
if zone_risk > 2500:
    st.error("🚨 EXTREME DANGER ZONE")
elif zone_risk > 1200:
    st.warning("⚠️ HIGH RISK ZONE")
else:
    st.success("✅ RELATIVELY SAFE ZONE")

st.progress(min(zone_risk / 3000, 1.0))

# Bar chart
st.subheader("📊 Danger Statistics")

top10 = df.sort_values("DANGER_SCORE", ascending=False).head(10)

fig1 = px.bar(
    top10,
    x="DISTRICT",
    y="DANGER_SCORE",
    color="DANGER_SCORE",
    title="Top Dangerous Districts"
)

st.plotly_chart(fig1, use_container_width=True)
