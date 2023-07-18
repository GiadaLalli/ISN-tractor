"""Plot filtration curve for the publication."""

import sys

import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

import isn_tractor.ibisn as it


def analyze_network_data(df, abs_val=True, thr_values=None, label_column="label", output=None):
    """Preprocess data by label."""
    if thr_values is None:
        thr_values = np.arange(-4, 4, 0.03)

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
            for i, thr_value in enumerate(thr_values):
                Adj_bin = np.where((Adj > thr_value) & (Adj != 0), 1, 0)
                g = nx.from_numpy_array(Adj_bin, create_using=nx.Graph)
                FCs[label][indv, i] = g.number_of_edges()

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

    if output is None:
        plt.show()
    else:
        plt.savefig(output)

if __name__ == "__main__":
    # Load in data
    expr_filename = sys.argv[1]
    clinic_filename = sys.argv[2]
    subset = int(sys.argv[3])
    output = sys.argv[4] if sys.argv[4] != "-" else None
    # expr = read_r(expr_filename)[None]
    # expr = np.load(expr_filename)
    expr = pd.read_csv(expr_filename, sep=' ', index_col=0)
    #expr = pd.DataFrame(expr, columns=['gene' + str(i+1) for i in range(expr.shape[1])])
    clinic = pd.read_csv(clinic_filename, sep=' ')
    print(expr.shape)
    print(clinic.shape)
    print(expr.head())
    print(clinic.head())
    # sys.exit()
    # Select the most variable features
    variance = np.argsort(np.var(expr, axis=0))[::-1]
    expr = expr.iloc[:subset, variance[:subset]]
    clinic = clinic.iloc[:subset]

    # ISN computation
    print(expr.shape)
    ISNs = pd.DataFrame(it.dense_isn(expr)).astype(float)
    a = np.repeat(expr.columns, expr.shape[1])
    b = np.tile(expr.columns, expr.shape[1])
    ISNs.columns = [a[i]+'_'+b[i] for i in range(expr.shape[1]**2)]

    # Filtration curve
    df = pd.concat([ISNs, clinic['mets']], axis=1)
    analyze_network_data(df.iloc[:20], label_column='mets', abs_val=False, output=output)