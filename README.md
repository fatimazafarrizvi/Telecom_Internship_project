# 📡 Telecom Network KPI Monitoring System

A professional **Streamlit-based dashboard** that simulates a **Bharti Airtel-style telecom monitoring system**, inspired by real internship experience in the Mobility Network Department.

## 🎯 Overview

This project demonstrates how telecom operators monitor and optimize network performance using real KPI data. It replicates professional tools like **GLIMS, Mycom & Actix** for visualizing RAN (Radio Access Network) performance metrics.

### Key Features

| Feature | Description |
|---------|-------------|
| 📊 **KPI Dashboard** | Pre vs Post outage KPI comparison across 10 clusters |
| 📅 **Yearly Trends** | Line charts and cumulative Ogive trends for 365 days |
| 📍 **Cluster Analytics** | Per-cluster performance analysis with interactive filters |
| 🧾 **Insights Engine** | Auto-generated performance insights and network health verdict |
| 🎨 **Interactive Visualizations** | Plotly-powered interactive charts and data tables |

---

## 📚 Project Structure

```
Telecom_Internship_project1/
├── Home.py                          # Main landing page
├── data_generator.py                # Synthetic data generation
├── utils.py                         # Utility functions
├── requirements.txt                 # Python dependencies
├── README.md                        # Project documentation
├── images/                          # Network architecture diagrams
│   ├── network_architecture_example.png
│   ├── ran_sector_diagram.png
│   └── tilt_example.png
└── pages/                           # Streamlit multi-page app
    ├── 1_Dashboard.py               # Pre vs Post KPI comparison
    ├── 2_Trends.py                  # Yearly trends & Ogive
    ├── 3_Cluster_Analytics.py       # Cluster-wise analysis
    └── 4_Insights.py                # Auto-generated insights
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)


## 📖 Page Guide

### 🏠 Home Page (`Home.py`)
- **Purpose**: Introduction and educational content
- **Content**:
  - Project overview and internship context
  - RAN Operations (2G/4G/5G architecture)
  - Transmission & Optical Fiber details
  - OHS (Occupational Health & Safety) guidelines
  - WFM (Workforce Management) overview
  - EMF Radiation compliance info
  - Network KPIs and optimization cycles
  - NOC (Network Operations Centre) explanation

### 📊 Dashboard Page (`pages/1_Dashboard.py`)
- **Purpose**: Compare KPI performance before and after optimizations
- **Features**:
  - Pre vs Post value comparison
  - Status indicators (Improved/Degraded)
  - Percentage change calculations
  - Interactive bar charts by cluster
  - Selectable KPI visualization

**KPIs Tracked**:
- **DL_Throughput** - Download speed (Mbps)
- **UL_Throughput** - Upload speed (Mbps)
- **Handover_Success** - Successful handover rate (%)
- **Paging_Success** - Paging success rate (%)
- **RLF** - Radio Link Failure count (lower is better)

### 📅 Trends Page (`pages/2_Trends.py`)
- **Purpose**: Analyze KPI performance over 365 days
- **Features**:
  - Daily trend line charts
  - Cumulative Ogive visualization
  - Cluster selection filter
  - KPI selection dropdown

### 📍 Cluster Analytics Page (`pages/3_Cluster_Analytics.py`)
- **Purpose**: Deep-dive into individual cluster performance
- **Features**:
  - Cluster selection from 10 available clusters
  - Throughput trend visualization
  - Data table preview

### 🧾 Insights Page (`pages/4_Insights.py`)
- **Purpose**: Auto-generated performance insights
- **Features**:
  - Summary report (total improvements vs degradations)
  - KPI-wise insight cards
  - Overall network health verdict
  - Color-coded status indicators

---

## 🔧 Technical Stack

| Component | Technology |
|-----------|-----------|
| **Frontend Framework** | Streamlit |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Plotly Express |
| **Data Generation** | NumPy (seeded for reproducibility) |
| **Language** | Python 3.8+ |

---

## 📊 Data Generation Details

### [data_generator.py](data_generator.py)

The synthetic data generation follows realistic telecom patterns:

- **10 Clusters** (CLU001 to CLU010)
- **365-day period** (2024-01-01 to 2024-12-31)
- **KPI Changes**:
  - 80% probability of improvement
  - 20% probability of degradation
  - Controlled ranges for realistic variations

**Generated Datasets**:
1. `df` - Pre vs Post comparison (10 rows, one per cluster)
2. `df_year` - Daily KPI values (3650 rows = 10 clusters × 365 days)
3. `df_cum` - Cumulative Ogive data (for trend analysis)

---

## 🛠️ Key Functions

### [utils.py](utils.py)

```python
def status(val, invert=False):
    """
    Determine if a KPI change represents improvement or degradation.
    
    Args:
        val (float): The change value
        invert (bool): If True, negative change = improvement (used for RLF)
    
    Returns:
        str: "Improved" or "Degraded"
    """
```

---

## 📈 KPI Definitions

| KPI | Target | Unit | Better Direction |
|-----|--------|------|-----------------|
| **CSSR** (Call Setup Success Rate) | >99.5% | % | Higher |
| **DCR** (Drop Call Rate) | <1% | % | Lower |
| **HOSR** (Handover Success Rate) | >98% | % | Higher |
| **DL Throughput** | 20-35 | Mbps | Higher |
| **UL Throughput** | 5-15 | Mbps | Higher |
| **RLF** (Radio Link Failure) | <2 | Count | Lower |
| **RSRP/RSRQ/SINR** | Varies | dBm | Higher |

---

## 🎓 Internship Learnings

This project incorporates real telecom concepts from the **Bharti Airtel Mobility Network Department**:

### RAN Operations
- **4G LTE**: eNodeB, EPC (MME, S-GW, P-GW, HSS, PCRF)
- **5G**: NSA/SA modes, Network Slicing (eMBB, mMTC, URLLC)
- **Site Architecture**: 3-sector configurations, frequency layers (900/1800/2100/2300/3500 MHz)

### Transmission
- **Microwave (MW)**: ODU + IDU, rain/fog dependent
- **Optical Fiber**: High capacity, low latency
- **CSR**: Dual-path routing (Fiber primary, MW backup)

### Operations
- **NOC**: 24x7 network monitoring, escalation handling
- **OHS**: 5 Golden Safety Rules compliance
- **WFM**: Ticketing, spare management (Oracle + CATS app)
- **EMF**: Radiation compliance audits (DoT & ICNIRP limits)

---

## 💡 Use Cases

1. **Network Optimization Teams**: Monitor KPI improvements post-optimization
2. **NOC Operations**: Quick insights into network health
3. **Data Analysis Training**: Learn how telecom KPIs are tracked
4. **Internship Portfolio**: Demonstrate real-world telecom knowledge
5. **Stakeholder Reporting**: Visualize network performance trends

---

## 👤 Author

**Fatima** - Telecom Network Internship Project  
*Based on real Bharti Airtel internship experience in the Mobility Network Department*

---

## 🙏 Acknowledgments

- Bharti Airtel Limited for internship insights
- Streamlit for the amazing dashboard framework
- Plotly for interactive visualizations
- Pandas & NumPy for data processing

---

## 📧 Contact & Support

For questions or suggestions, feel free to reach out or open an issue on GitHub.

**Happy Monitoring! 📡**
