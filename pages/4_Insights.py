import streamlit as st
from data_generator import generate_data
from utils import status

df, df_year, df_cum, clusters = generate_data()

st.title("🧾 Automatically Generated Insights")

# ---------------------------------------------------
# FIX: Add KPI change + status calculation here
# ---------------------------------------------------

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


# ---------- SUMMARY SECTION ----------
improve = (df.filter(like="Status") == "Improved").sum().sum()
degrade = (df.filter(like="Status") == "Degraded").sum().sum()

st.subheader("📌 Summary Report")
st.write(f"✔ Total Improvements: **{improve}**")
st.write(f"⚠ Total Degradations: **{degrade}**")


# ---------- ADD YOUR KPI-WISE INSIGHTS HERE ----------
st.subheader("📍 KPI-wise Insights")

kpis = ["DL_Status", "UL_Status", "Handover_Status", "Paging_Status", "RLF_Status"]

for kpi in kpis:
    improved = (df[kpi] == "Improved").sum()
    degraded = (df[kpi] == "Degraded").sum()

    if improved > degraded:
        st.success(f"{kpi.replace('_', ' ')} mostly improved.")
    else:
        st.error(f"{kpi.replace('_', ' ')} needs optimization.")


# ---------- OPTIONAL OVERALL VERDICT ----------
st.markdown("---")
st.subheader("📊 Overall Network Insight")

if improve > degrade:
    st.success("Overall network health shows improvements in the monitored period.")
elif improve == degrade:
    st.info("Network performance is stable with balanced improvements and degradations.")
else:
    st.warning("Some KPIs show degradation — further optimization recommended.")
