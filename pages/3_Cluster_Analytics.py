import streamlit as st
import plotly.express as px
from data_generator import generate_data

df, df_year, df_cum, clusters = generate_data()

st.title("📈 Cluster Analytics")

cluster = st.selectbox("Select Cluster", clusters)

df_cluster = df_year[df_year["ClusterID"] == cluster]

st.subheader("Cluster Data")
st.dataframe(df_cluster.head())

fig = px.line(df_cluster, x="Date", y=["DL_Throughput","UL_Throughput"], title="Throughput Trends")
st.plotly_chart(fig, use_container_width=True)
