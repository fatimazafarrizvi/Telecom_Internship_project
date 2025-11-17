import streamlit as st

st.set_page_config(page_title="Network KPI Dashboard", layout="wide")

st.title("📡 Telecom Network KPI Monitoring System")
st.markdown("---")

# =============================
# INTRODUCTION
# =============================
st.header("📘 Introduction")
st.markdown("""
This project simulates a **Bharti Airtel–style professional telecom monitoring system**.  
It is inspired by my internship in the **Mobility Network Department**, where I learned how real operators monitor:

- **RAN Performance (2G/4G/5G)**
- **Transmission (MW, Fiber, UBR)**
- **Network KPIs & Optimization**
- **NOC Operations**
- **OHS, EMF, WFM Processes**

This dashboard replicates how tools like **GLIMS, Mycom & Actix** visualize telecom KPIs.

---
""")

# OPTIONAL IMAGE (UPLOAD LATER)
st.image("images/network_architecture_example.png", caption="4G / 5G RAN Architecture (Illustration)", use_container_width=True)

# =============================
# RAN OPERATIONS
# =============================
st.header("📶 Radio Access Network (RAN) Operations – 2G | 4G LTE | 5G")
st.markdown("""
The **Radio Access Network (RAN)** is the bridge between mobile users (UE) and the operator's core network.  
This includes:

### 🔹 4G LTE Architecture
- **eNodeB** performs scheduling, RRM, handovers.
- **EPC Core Components:**
  - **MME** – signaling + mobility  
  - **S-GW** – user-plane router  
  - **P-GW** – internet gateway  
  - **HSS** – subscriber database  
  - **PCRF** – QoS & policy  

### 🔹 5G Architecture – NSA & SA
- **NSA (Non-Standalone)** uses 4G as anchor + 5G as booster  
- **SA (Standalone)** uses a new 5G Core with **AMF, SMF, UPF**
- **Network Slicing** enables eMBB, mMTC, and URLLC slices

### 🔹 RAN Key Concepts
- **Cells & Sectors** (3-sector sites)
- **Frequency Layers** (900/1800/2100/2300/3500 MHz)
- **PCI (Physical Cell ID)**
""")

# IMAGE PLACEHOLDER
st.image("images/ran_sector_diagram.png", caption="Typical 3-Sector Telecom Site", use_container_width=True)

st.markdown("---")

# =============================
# TRANSMISSION
# =============================
st.header("🛰 Transmission & Optical Fiber")
st.markdown("""
### Microwave (MW)
- Consists of **ODU + IDU**
- Used in hilly or remote areas
- Affected by rain, fog (LOS dependent)

### Optical Fiber
- Highest capacity  
- Very low latency  
- Used in most urban deployments  

### CSR Architecture
A **Cell Site Router (CSR)** ensures dual path:
- Fiber (Primary)
- MW (Backup)
""")

# =============================
# OHS
# =============================
st.header("🦺 Occupational Health & Safety (OHS)")
st.markdown("""
Airtel enforces strict **5 Golden Safety Rules**:

1. Seat Belts Mandatory  
2. No Helmet → No Ride  
3. No Over-speeding  
4. No PPE → No Work  
5. Permit-to-Work (PTW) is compulsory  
""")

st.markdown("---")

# =============================
# WFM
# =============================
st.header("🔧 Workforce & Spare Management (WFM)")
st.markdown("""
- OSS alarms monitored in real-time  
- Auto ticketing to field teams  
- Spare stock managed through Oracle system  
- Serial-based spare tracking through **CATS mobile app**
""")

# =============================
# EMF
# =============================
st.header("📡 EMF Radiation Compliance")
st.markdown("""
Airtel follows strict DoT & ICNIRP EMF limits.  
Sites undergo regular **EMF audits** to ensure radiation is safe for the public.
""")

st.markdown("---")

# =============================
# NETWORK KPIs & NPO
# =============================
st.header("📊 Network Performance & Optimization (NPO)")
st.subheader("Key Performance Indicators (KPIs)")
st.markdown("""
- **CSSR** – >99.5%  
- **DCR** – <1%  
- **HOSR** – Successful handovers  
- **DL/UL Throughput** – User’s data speeds  
- **Payload** – Traffic volume  
- **RSRP / RSRQ / SINR** – Coverage & quality  
""")

st.subheader("Optimization Cycle")
st.markdown("""
1. Identify faulty cells  
2. Analyze coverage/interference/utilization  
3. Fix (tilt, azimuth, PCI, power, hardware)  
4. Verify performance improvement  
""")

# IMAGE PLACEHOLDER
st.image("images/tilt_example.png", caption="Antenna Tilt & Azimuth Optimization", use_container_width=True)

st.markdown("---")

# =============================
# NOC
# =============================
st.header("🖥 Network Operations Centre (NOC)")
st.markdown("""
The **NOC** is the central command center:

- Monitors entire network 24x7  
- Handles outages & escalations  
- Coordinates RAN, Core, Transmission teams  

**LNOC** – State-level  
**OMCR** – Radio-specific network monitoring  
""")

st.markdown("---")

# =============================
# PROJECT PURPOSE
# =============================
st.header("🎯 Purpose of This Dashboard")
st.markdown("""
This system demonstrates a **real telecom workflow**:

| Feature | Description |
|--------|-------------|
| 📊 KPI Dashboard | Compares Pre vs Post outage KPIs |
| 📆 Year Trends | Line & Ogive trends for 365 days |
| 📍 Cluster Analytics | Per-cluster performance with filters |
| 🤖 Insights Engine | Auto-generated performance insights |

This project reflects how real telecom teams analyze data daily.
""")

st.markdown("---")
st.success("This Home Page content was created using real data & explanations from the Bharti Airtel internship report document.")
