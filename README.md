# Voltage Time-Series Analysis and Interactive Dashboard

This project presents a complete time-series analysis of voltage data, starting from raw data visualization to advanced event detection and interactive exploration using a web-based dashboard.

The analysis was initially developed in a Jupyter Notebook and later converted into a serially ordered, interactive Streamlit application for better visualization, interpretation, and usability.

---

## 📁 Project Structure

voltage-analysis/
│── app.py # Streamlit dashboard application

│── Sample_Data.csv # Input dataset (Timestamp, Voltage)

│── README.md # Project documentation

│── Voltage_Peaks_Lows.csv # Exported peaks and lows

│── Voltage_Below_30.csv # Exported low-voltage events

│── Downward_Slope_Acceleration.csv # Exported acceleration events

---

## 📊 Dataset Description

The dataset consists of real-time voltage readings captured at frequent intervals.

| Column Name | Description |
|------------|------------|
| Timestamp  | Date and time of voltage reading |
| Values     | Voltage value at that timestamp |

The data spans multiple days and contains both stable periods and repeated voltage drops.

---

## 🧠 Analysis Workflow (Serial Order)

The Streamlit dashboard follows the **same sequential order** as the original Jupyter Notebook:

### 1. Data Loading and Inspection
- Data is loaded from CSV
- Timestamp is parsed into datetime format
- Data is sorted chronologically

---

### 2. Voltage vs Timestamp Visualization
- A raw time-series plot shows voltage variation over time
- Helps identify overall patterns and fluctuations

---

### 3. Data Smoothing (Rolling Average)
- A rolling (moving) average is applied to reduce short-term noise
- Makes long-term trends easier to observe
---
4. Local Peaks and Lows Detection
- Peaks: local maximum voltage points
- Lows: local minimum voltage points
- Detected using signal processing techniques
---
5. Peaks and Lows Visualization
- Peaks and lows are overlaid on the voltage plot
- Helps visually locate significant turning points
---
6. Low Voltage Event Detection
- Filters all instances where voltage drops below a defined threshold
---
7. Downward Slope and Acceleration Analysis
- Slope: rate of voltage change
- Acceleration: change in slope
- Used to detect rapidly worsening voltage drops
---
8. Downward Acceleration Event Detection
- Events are detected when:
           - Voltage is decreasing rapidly (steep slope), OR
           - The rate of decrease increases suddenly (negative acceleration)
           - Interactive sliders allow tuning detection sensitivity.
---
9. Event Visualization
- Acceleration events are highlighted on the voltage plot
-  Allows quick identification of critical drop moments
---
10. Tabular Outputs
- Peaks and lows table
- Acceleration events table
- Low-voltage events table

All tables are scrollable and exportable

🎛 Interactive Dashboard (Streamlit)

The Streamlit dashboard provides:

- Sequential presentation (same order as notebook)

- Interactive sliders for sensitivity control

- Clean and responsive UI

- Dynamic plots and tables

- Real-time updates based on user input

Run the dashboard locally:
streamlit run app.py


The application will open at:
https://analysis-of-voltage-and-timestamp-kx6almdxwmydbtdddrdugt.streamlit.app/

🧪 Dependencies

Install required libraries using:

pip install pandas numpy matplotlib scipy streamlit

📈 Key Insights

- Voltage shows repeated cyclical drops rather than random noise

- Rolling averages reveal long-term stability patterns

- Local peaks and lows identify turning points

- Acceleration-based detection captures rapid voltage deterioration

- No voltage readings were observed below 20 units

- Several moderate voltage drops (<30) were detected

🧠 Use Cases

- Electrical system monitoring

- Signal and time-series analysis

- Fault and anomaly detection

- Engineering diagnostics

- Interactive data visualization

- Academic and portfolio projects

🚀 Future Enhancements

- Predictive modeling (ARIMA / LSTM)

- Automatic threshold recommendation


