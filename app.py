import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Battery Energy Storage System Dashboard")

data = pd.read_csv("bess_energy_dataset.csv")

st.subheader("Dataset Preview")
st.write(data.head())

st.subheader("Energy Consumption Graph")

fig, ax = plt.subplots()
ax.plot(data.iloc[:,1])
ax.set_ylabel("Energy Consumption (MW)")
st.pyplot(fig)