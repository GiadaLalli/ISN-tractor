"""Plot filtration curve for the publication."""

import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def analyze_network_data(df, abs_val=True, thr_values=None, label_column="label"):
    """Preprocess data by label."""
    if thr_values is None:
        thr_values = np.arange(0.02, 4, 0.03)

    labels = np.sort(df[label_column].unique())
    print(labels)

    df.index.name = None

    data = []
    for label in labels:
        data_label = df[df[label_column] == label]

        data_label.drop([label_column], axis=1, inplace=True)

        data_label = data_label.T.reset_index()

        data_label[["N1", "N2"]] = data_label["index"].str.split("_", expand=True)
        data_label.drop(["index"], axis=1, inplace=True)

        data.append(data_label)

    data_list = [{} for i in labels]
    for label in range(len(labels)):
        for i in range(data[label].shape[1] - 2):
            temp = (
                data[label]
                .iloc[:, [data[label].shape[1] - 2, data[label].shape[1] - 1, i]]
                .copy()
            )
            if abs_val:
                temp.iloc[:, 2] = np.abs(temp.iloc[:, 2])
            aa = temp.columns[2]
            temp.columns = ["E1", "E2", "Weight"]
            mygraph = nx.from_pandas_edgelist(temp, "E1", "E2", "Weight")
            gg = nx.to_numpy_array(mygraph, weight="Weight")
            data_list[label][aa] = gg

    FCs = []
    for i in range(len(labels)):
        FC = np.zeros((len(data_list[i]), len(thr_values)))
        FCs.append(FC)

    for label in range(len(labels)):
        for indv in range(len(data_list[label])):
            nm_l = list(data_list[label].keys())[indv]
            Adj = data_list[label][nm_l]
            for i, thr_value in range(len(thr_values)):
                Adj_bin = np.where((Adj < thr_value) & (Adj > 0), 1, 0)
                g = nx.from_numpy_array(Adj_bin, create_using=nx.Graph)
                FCs[label][indv, i] = g.size()

    df = []
    for i in range(len(labels)):
        df.append(
            pd.DataFrame(
                {
                    "Thr": thr_values,
                    "Mean": np.mean(FCs[i], axis=0),
                    "sd": np.std(FCs[i], axis=0),
                    "cl": ["Cluster " + str(i + 1)] * len(thr_values),
                }
            )
        )

    plt.figure(figsize=(12, 10))
    for i in range(len(labels)):
        plt.errorbar(
            df[i]["Thr"],
            df[i]["Mean"],
            yerr=df[i]["sd"],
            elinewidth=0.5,
            label="Cluster " + str(i + 1),
        )

    plt.xlabel("Threshold Values", fontsize=20)
    plt.ylabel("Graph Statistic: Strength", fontsize=20)

    leg = plt.legend(loc="upper left", fontsize=15)
    for line in leg.get_lines():
        line.set_linewidth(10)

    plt.show()
