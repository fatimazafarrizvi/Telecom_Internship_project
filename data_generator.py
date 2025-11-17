import pandas as pd
import numpy as np

np.random.seed(42)

def generate_data():
    clusters = [f"CLU{str(i).zfill(3)}" for i in range(1, 11)]
    dates = pd.date_range("2024-01-01", periods=365)

    # Pre values only
    data = {
        "ClusterID": clusters,
        "DL_Throughput_Pre": np.random.uniform(20, 35, 10),
        "UL_Throughput_Pre": np.random.uniform(5, 15, 10),
        "Handover_Success_Pre": np.random.uniform(90, 99, 10),
        "Paging_Success_Pre": np.random.uniform(85, 98, 10),
        "RLF_Pre": np.random.uniform(0.5, 2.0, 10),
    }

    df = pd.DataFrame(data)

    # Post values derived from Pre (controlled)
    def random_change(pre_array, improve_range, degrade_range, improve_prob=0.8):
        post = []
        for pre in pre_array:
            if np.random.rand() < improve_prob:   # 80% chance improve
                post.append(pre + np.random.uniform(*improve_range))
            else:                                 # 20% chance degrade
                post.append(pre - np.random.uniform(*degrade_range))
        return np.array(post)

    # Apply to each KPI
    df["DL_Throughput_Post"] = random_change(df["DL_Throughput_Pre"], (1, 5), (0.5, 2))
    df["UL_Throughput_Post"] = random_change(df["UL_Throughput_Pre"], (0.5, 3), (0.2, 1))
    df["Handover_Success_Post"] = random_change(df["Handover_Success_Pre"], (0.5, 1.5), (0.2, 1))
    df["Paging_Success_Post"] = random_change(df["Paging_Success_Pre"], (0.5, 1.2), (0.2, 1))

    # RLF – negative change = improvement
    df["RLF_Post"] = random_change(df["RLF_Pre"], (-0.5, -0.1), (0.1, 0.3))

    # Generate 1-year trend dataset
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

    df_cum = (
        df_year
        .groupby(["ClusterID", "Date"])
        .mean()
        .groupby(level=0)
        .cumsum()
        .reset_index()
    )

    return df, df_year, df_cum, clusters

