import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from scipy.signal import find_peaks

st.set_page_config(
    page_title="Voltage Analysis (Serial View)",
    layout="wide"
)

st.title("Voltage Analysis Dashboard")
st.caption("Serial presentation of analysis of Voltage and Timestamps")

st.header("1. Data Loading")

df = pd.read_csv("Sample_Data.csv")
df['Timestamp'] = pd.to_datetime(df['Timestamp'], dayfirst=True)
df = df.sort_values('Timestamp').reset_index(drop=True)

st.write("Sample of dataset:")
st.dataframe(df.head(), use_container_width=True)

st.header("2. Voltage vs Timestamp")

fig, ax = plt.subplots(figsize=(12,4))
ax.plot(df['Timestamp'], df['Values'], linewidth=1)
ax.set_xlabel("Timestamp")
ax.set_ylabel("Voltage")
ax.grid(True)
st.pyplot(fig)

st.header("3. Data Smoothing")

window = st.slider("Rolling window size", 5, 200, 50)

df['Rolling_Avg'] = df['Values'].rolling(window).mean()

fig, ax = plt.subplots(figsize=(12,4))
ax.plot(df['Timestamp'], df['Values'], alpha=0.4, label="Raw Voltage")
ax.plot(df['Timestamp'], df['Rolling_Avg'], color="red", label="Rolling Average")
ax.legend()
ax.grid(True)
st.pyplot(fig)

st.header("4. Local Peaks and Lows Detection")

peaks, _ = find_peaks(df['Values'], distance=10)
lows, _ = find_peaks(-df['Values'], distance=10)

peaks_df = df.iloc[peaks][['Timestamp', 'Values']]
peaks_df['Type'] = "Peak"

lows_df = df.iloc[lows][['Timestamp', 'Values']]
lows_df['Type'] = "Low"

peaks_lows_df = pd.concat([peaks_df, lows_df]).sort_values('Timestamp')

st.write("Detected Peaks and Lows:")
st.dataframe(peaks_lows_df, height=300, use_container_width=True)
st.header("5. Peaks and Lows Visualization")

fig, ax = plt.subplots(figsize=(12,4))
ax.plot(df['Timestamp'], df['Values'], linewidth=1)
ax.scatter(peaks_df['Timestamp'], peaks_df['Values'], color="green", s=20, label="Peaks")
ax.scatter(lows_df['Timestamp'], lows_df['Values'], color="red", s=20, label="Lows")
ax.legend()
ax.grid(True)
st.pyplot(fig)

st.header("6. Voltage Below Threshold")

threshold = st.slider("Voltage threshold", 10, 50, 20)

low_voltage_df = df[df['Values'] < threshold]

st.write(f"Instances where voltage < {threshold}:")
st.dataframe(low_voltage_df[['Timestamp', 'Values']], use_container_width=True)

st.metric("Count", len(low_voltage_df))

st.header("7. Downward Slope & Acceleration Analysis")

df['Slope'] = df['Values'].diff()
df['Acceleration'] = df['Slope'].diff()

st.write("Computed slope and acceleration:")
st.dataframe(df[['Timestamp', 'Values', 'Slope', 'Acceleration']].head(),
             use_container_width=True)

st.header("8. Downward Acceleration Events")

slope_th = st.slider("Slope sensitivity", 1, 10, 2)
acc_th = st.slider("Acceleration sensitivity", 0, 10, 1)

acc_events = df[
    (df['Slope'] < -slope_th) |
    (df['Acceleration'] < -acc_th)
]

st.write("Detected acceleration events:")
st.dataframe(
    acc_events[['Timestamp', 'Values', 'Slope', 'Acceleration']],
    height=300,
    use_container_width=True
)

st.header("9. Acceleration Events Visualization")

fig, ax = plt.subplots(figsize=(12,4))
ax.plot(df['Timestamp'], df['Values'], linewidth=1)
ax.scatter(acc_events['Timestamp'], acc_events['Values'],
           color="orange", s=25, label="Acceleration Events")
ax.legend()
ax.grid(True)
st.pyplot(fig)

st.header("10. Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Total Records", len(df))
col2.metric("Peaks", len(peaks_df))
col3.metric("Acceleration Events", len(acc_events))

