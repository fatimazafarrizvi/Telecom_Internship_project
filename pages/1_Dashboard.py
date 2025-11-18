import streamlit as st
import plotly.express as px
from data_generator import generate_data
from utils import status

df, df_year, df_cum, clusters = generate_data()

st.title("📊 Pre vs Post KPI Comparison")

# Calculate status columns
df["DL_Change(%)"] = ((df["DL_Throughput_Post"] - df["DL_Throughput_Pre"]) / df["DL_Throughput_Pre"]) * 100
df["UL_Change(%)"] = ((df["UL_Throughput_Post"] - df["UL_Throughput_Pre"]) / df["UL_Throughput_Pre"]) * 100
df["Handover_Change(%)"] = df["Handover_Success_Post"] - df["Handover_Success_Pre"]
df["Paging_Change(%)"] = df["Paging_Success_Post"] - df["Paging_Success_Pre"]
df["RLF_Change(%)"] = df["RLF_Post"] - df["RLF_Pre"]

df["DL_Status"] = df["DL_Change(%)"].apply(status)
df["UL_Status"] = df["UL_Change(%)"].apply(status)
df["Handover_Status"] = df["Handover_Change(%)"].apply(status)
df["Paging_Status"] = df["Paging_Change(%)"].apply(status)
df["RLF_Status"] = df["RLF_Change(%)"].apply(lambda x: status(x, invert=True))

#st.dataframe(df)

st.subheader("📈 Compare KPI (Cluster-wise)")
st.dataframe(df.style.map(lambda x: "background-color: green" if x=="Improved" else "background-color: red" if x=="Degraded" else ""))

kpi_choice = st.selectbox("Select KPI", ["DL_Throughput", "UL_Throughput", "Handover_Success", "Paging_Success", "RLF"])

fig = px.bar(df,
             x="ClusterID",
             y=[f"{kpi_choice}_Pre", f"{kpi_choice}_Post"],
             barmode="group",
             title=f"{kpi_choice} Pre vs Post")
st.plotly_chart(fig, use_container_width=True)
