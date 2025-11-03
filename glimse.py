import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

np.random.seed(42)
clusters = [f"CLU{str(i).zfill(3)}" for i in range(1, 11)]
dates = pd.date_range("2024-01-01", periods=365)

data = {
    "ClusterID": clusters,
    "DL_Throughput_Pre": np.random.uniform(20, 35, 10),
    "DL_Throughput_Post": np.random.uniform(20, 35, 10),
    "UL_Throughput_Pre": np.random.uniform(5, 15, 10),
    "UL_Throughput_Post": np.random.uniform(5, 15, 10),
    "Handover_Success_Pre": np.random.uniform(90, 99, 10),
    "Handover_Success_Post": np.random.uniform(90, 99, 10),
    "Paging_Success_Pre": np.random.uniform(85, 98, 10),
    "Paging_Success_Post": np.random.uniform(85, 98, 10),
    "RLF_Pre": np.random.uniform(0.5, 2.0, 10),
    "RLF_Post": np.random.uniform(0.5, 2.0, 10)
}

df = pd.DataFrame(data)

records = []
for clu in clusters:
    dl_base = np.random.uniform(20, 35)
    ul_base = np.random.uniform(5, 15)
    ho_base = np.random.uniform(90, 99)
    pg_base = np.random.uniform(85, 98)
    rlf_base = np.random.uniform(0.5, 2.0)

    for d in dates:
        records.append({
            "Date": d,
            "ClusterID": clu,
            "DL_Throughput": dl_base + np.random.normal(0, 1),
            "UL_Throughput": ul_base + np.random.normal(0, 0.5),
            "Handover_Success": ho_base + np.random.normal(0, 0.3),
            "Paging_Success": pg_base + np.random.normal(0, 0.4),
            "RLF": abs(rlf_base + np.random.normal(0, 0.05))
        })

df_year = pd.DataFrame(records)

df["DL_Change(%)"] = ((df["DL_Throughput_Post"] - df["DL_Throughput_Pre"]) / df["DL_Throughput_Pre"]) * 100
df["UL_Change(%)"] = ((df["UL_Throughput_Post"] - df["UL_Throughput_Pre"]) / df["UL_Throughput_Pre"]) * 100
df["Handover_Change(%)"] = df["Handover_Success_Post"] - df["Handover_Success_Pre"]
df["Paging_Change(%)"] = df["Paging_Success_Post"] - df["Paging_Success_Pre"]
df["RLF_Change(%)"] = df["RLF_Post"] - df["RLF_Pre"]

# Label function
def status(val, invert=False):
    if invert:  # for RLF (lower = better)
        return "Improved" if val < 0 else "Degraded"
    else:
        return "Improved" if val > 0 else "Degraded"

df["DL_Status"] = df["DL_Change(%)"].apply(status)
df["UL_Status"] = df["UL_Change(%)"].apply(status)
df["Handover_Status"] = df["Handover_Change(%)"].apply(status)
df["Paging_Status"] = df["Paging_Change(%)"].apply(status)
df["RLF_Status"] = df["RLF_Change(%)"].apply(lambda x: status(x, invert=True))

#cumulative average per cluster
df_cum = (
    df_year
    .groupby(["ClusterID", "Date"])
    .mean()
    .groupby(level=0)
    .cumsum()
    .reset_index()
)

st.set_page_config(page_title="Network KPI Dashboard", layout="wide")

st.title("📊 Network KPI Dashboard ")
st.markdown("This dashboard shows **Pre vs Post outage KPIs** with improvements and degradations comparing two months data.")

# Show raw table
st.subheader("Cluster KPI Data")
st.dataframe(df.style.applymap(lambda x: "background-color: green" if x=="Improved" else "background-color: red" if x=="Degraded" else ""))

# -------------------------------
# STEP 4: Interactive Charts
# -------------------------------
st.subheader("📈 KPI Trends per Cluster")

kpi_choice = st.selectbox("Select KPI to Compare the data for the last two months.", ["DL_Throughput", "UL_Throughput", "Handover_Success", "Paging_Success", "RLF"])

fig = px.bar(
    df,
    x="ClusterID",
    y=[f"{kpi_choice}_Pre", f"{kpi_choice}_Post"],
    barmode="group",
    text_auto=True,
    title=f"{kpi_choice} Pre vs Post"
)
st.plotly_chart(fig, use_container_width=True)

# -------------------------------
# STEP 4: Select KPI for Visualization
# -------------------------------
kpi_choice = st.selectbox(
    "Select KPI to View Trend",
    ["DL_Throughput", "UL_Throughput", "Handover_Success", "Paging_Success", "RLF"]
)

cluster_choice = st.selectbox("Select Cluster", clusters)

# Filter data
df_cluster = df_year[df_year["ClusterID"] == cluster_choice]
df_cum_cluster = df_cum[df_cum["ClusterID"] == cluster_choice]

# -------------------------------
# STEP 5: Plot Daily Trend
# -------------------------------
st.subheader(f"📅 Daily Trend of {kpi_choice} for {cluster_choice}")
fig_line = px.line(
    df_cluster,
    x="Date",
    y=kpi_choice,
    title=f"{kpi_choice} Trend over One Year - {cluster_choice}",
)
st.plotly_chart(fig_line, use_container_width=True)

# -------------------------------
# STEP 6: Plot Ogive (Cumulative Frequency)
# -------------------------------
st.subheader(f"📈 Ogive (Cumulative Trend) for {kpi_choice}")
fig_ogive = px.line(
    df_cum_cluster,
    x="Date",
    y=kpi_choice,
    title=f"Cumulative Ogive of {kpi_choice} - {cluster_choice}",
    markers=True
)
st.plotly_chart(fig_ogive, use_container_width=True)

# -------------------------------
# STEP 7: Summary Statistics
# -------------------------------
st.subheader("📌 Summary Insights (Yearly)")
col1, col2, col3 = st.columns(3)
col1.metric("Highest Daily Value", round(df_cluster[kpi_choice].max(), 2))
col2.metric("Lowest Daily Value", round(df_cluster[kpi_choice].min(), 2))
col3.metric("Average (Mean)", round(df_cluster[kpi_choice].mean(), 2))

st.markdown("---")
st.write("📅 **Data Preview**")
st.dataframe(df_cluster.head())

