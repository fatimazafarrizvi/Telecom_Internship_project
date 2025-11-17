import streamlit as st
import plotly.express as px
from data_generator import generate_data

df, df_year, df_cum, clusters = generate_data()

st.title("📅 Yearly Trends & Ogive")

kpi_choice = st.selectbox("Select KPI", ["DL_Throughput", "UL_Throughput", "Handover_Success", "Paging_Success", "RLF"])
cluster_choice = st.selectbox("Select Cluster", clusters)

df_cluster = df_year[df_year["ClusterID"] == cluster_choice]
df_cum_cluster = df_cum[df_cum["ClusterID"] == cluster_choice]

st.subheader("📈 Daily Trend")
fig = px.line(df_cluster, x="Date", y=kpi_choice, title=f"{kpi_choice} Trend - {cluster_choice}")
st.plotly_chart(fig, use_container_width=True)

st.subheader("📈 Ogive Trend (Cumulative)")
fig2 = px.line(df_cum_cluster, x="Date", y=kpi_choice, markers=True, title=f"Cumulative Ogive - {cluster_choice}")
st.plotly_chart(fig2, use_container_width=True)
