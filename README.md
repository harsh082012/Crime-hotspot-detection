# 🚨 Delhi Road Accident Danger Map 🗺️

An interactive **Machine Learning + Geospatial Analytics** web app that predicts
🚦 road accident danger zones across Delhi using **DBSCAN clustering**, heatmaps,
and **live GPS safety detection**.

This project turns raw accident data into a smart city safety tool 💡.

---

## ✨ Features
- 🔢 Danger Score calculation from accident severity  
- 🧠 **DBSCAN (Density-Based Spatial Clustering)** for hotspot detection  
- 🌡️ Heatmap of accident intensity  
- 📍 Live user location safety check  
- 🎚️ Adjustable danger radius (2–15 km)  
- 📊 Top dangerous district analytics  
- 🌐 Interactive Streamlit dashboard  

---

## 🛠 Tech Stack
- 🐍 Python  
- 📊 Pandas, NumPy  
- 🤖 **Scikit-learn (DBSCAN)**  
- 🗺️ Folium, Leaflet  
- 🌐 Streamlit  
- 📈 Plotly  

---

## 🧠 Machine Learning Pipeline

1. **🧹 Data Cleaning**  
   Removed nulls, fixed district names, dropped unused columns.

2. **⚙️ Feature Engineering**  
   Built a `DANGER_SCORE` using injuries & fatalities.

3. **🤖 ML Clustering (DBSCAN)**  
   Grouped districts into **High / Moderate risk zones**  
   using density-based clustering.

4. **🗺️ Visualization**  
   Created heatmaps & bar charts.

5. **📍 Live Risk Detection**  
   Browser GPS → finds nearby danger zones → shows risk level.

---

## 🚀 Run Locally

```bash
pip install streamlit pandas numpy folium scikit-learn plotly streamlit-folium
streamlit run app.py
