"""Plot filtration curve for the publication."""

import sys

import pandas as pd
import numpy as np
from networkx import Graph, from_pandas_edgelist, to_numpy_array, from_numpy_array
import matplotlib.pyplot as plt

from isn_tractor.ibisn import dense_isn


def preprocess(data, label_column: str):
    """Seperate data into cases and controls and add necessary columns."""
    data.index.name = None

    controls = (
        data[data[label_column] == 0].drop([label_column], axis=1).T.reset_index()
    )
    cases = data[data[label_column] == 1].drop([label_column], axis=1).T.reset_index()
    controls[["N1", "N2"]] = controls["index"].str.split("_", expand=True)
    controls = controls.drop(["index"], axis=1)

    cases[["N1", "N2"]] = cases["index"].str.split("_", expand=True)
    cases = cases.drop(["index"], axis=1)

    return controls, cases


def graphs(data):
    """Compute graphs from ISNs."""
    data_list = {}
    for i in range(data.shape[1] - 2):
        temp = data.iloc[:, [data.shape[1] - 2, data.shape[1] - 1, i]].copy()
        key = temp.columns[2]
        temp.columns = ["E1", "E2", "Weight"]
        data_list[key] = to_numpy_array(
            from_pandas_edgelist(temp, "E1", "E2", "Weight"), weight="Weight"
        )

    return data_list


def calculate_filtration_curve(data_list, thr_values):
    """Apply the stat (number of graph edges) to the computed ISNs."""
    curve = np.zeros((len(data_list), len(thr_values)))
    for a, (individual, Adj) in enumerate(data_list.items()):
        for i, thr_value in enumerate(thr_values):
            curve[a, i] = from_numpy_array(
                np.where((Adj > thr_value) & (Adj != 0), 1, 0), create_using=Graph
            ).number_of_edges()

    return curve


def plot_filtration_curve(df, label_column="label", output=None):
    """Plot labeled data."""
    thr_values = np.arange(-4, 4, 0.03)

    controls_data, cases_data = preprocess(df, label_column)
    controls_FC = calculate_filtration_curve(graphs(controls_data), thr_values)
    cases_FC = calculate_filtration_curve(graphs(cases_data), thr_values)

    plt.figure(figsize=(12, 10))
    labels = {"Cases": "red", "Controls": "blue"}
    plt.errorbar(
        thr_values,
        np.mean(controls_FC, axis=0),
        yerr=np.std(controls_FC, axis=0),
        elinewidth=0.5,
    )
    plt.errorbar(
        thr_values,
        np.mean(cases_FC, axis=0),
        yerr=np.std(cases_FC, axis=0),
        elinewidth=0.5,
        color="red",
    )
    plt.xlabel("Threshold Values", fontsize=20)
    plt.ylabel("Graph Statistic: N Edges", fontsize=20)
    handles = [
        plt.Line2D([], [], color=labels[label], marker="o", linestyle="-")
        for label in labels
    ]
    plt.legend(handles, labels.keys(), loc="upper right", fontsize=15)

    if output is None:
        plt.show()
    else:
        plt.savefig(output)


def find_filter_edges(expr, sig):
    """Find the indexes of the columns we want to keep."""
    columns = np.asarray(
        [
            f"{a}_{b}"
            for (a, b) in zip(
                np.repeat(expr.columns, expr.shape[1]),
                np.tile(expr.columns, expr.shape[1]),
            )
        ]
    )
    sorter = np.argsort(columns)
    return sorter[np.searchsorted(columns, sig, sorter=sorter)]


TOP_EDGES = [
    "BGLAP_MMP11",
    "MFAP4_FKSG30",
    "MFAP4_CSPG2",
    "CSPG2_MXRA5",
    "COL8A1_H19",
    "PTHR1_DSPG3",
    "CXCL10_HOMER2",
    "CSPG2_DDIT4L",
    "TMSL8_SRPX",
    "BGLAP_HLA-DQB1",
    "PRSS35_HLA-DQB1",
    "AEBP1_SERPINE2",
    "FBLN2_CD248",
    "SULF1_CD248",
    "PHGDH_CDKN2A",
    "BGLAP_GZMA",
    "MFI2_GZMA",
    "RPS4Y1_SLC2A3",
    "FOS_SCIN",
    "CXCL9_SCIN",
    "SRPX_SCIN",
    "ENPP2_IFIT3",
    "TMSL8_SNAI2",
    "SULF1_SNAI2",
    "SNAI2_VWF",
    "ADM_LEPREL1",
    "SCRG1_AXL",
    "PLTP_IGFBP3",
    "MFAP4_SBDS",
    "SOST_STAT1",
    "IBSP_STAT1",
    "MEPE_STAT1",
    "IFITM5_STAT1",
    "KSP37_STAT1",
    "CDH15_STAT1",
    "PTHR1_STAT1",
    "TMEM119_STAT1",
    "SP7_STAT1",
    "MFI2_STAT1",
    "EFHD1_STAT1",
    "CCDC3_STAT1",
    "SEPP1_STAT1",
    "CD36_STAT1",
    "HOMER2_STAT1",
    "GYG2_STAT1",
    "ENPP2_STAT1",
    "ID3_STAT1",
    "SCIN_STAT1",
    "FOSB_SLC29A4",
    "SRPX_TNFSF10",
]

TOP_NODES = [
    "BGLAP",
    "MMP11",
    "MFAP4",
    "FKSG30",
    "CSPG2",
    "MXRA5",
    "COL8A1",
    "H19",
    "PTHR1",
    "DSPG3",
    "CXCL10",
    "HOMER2",
    "DDIT4L",
    "TMSL8",
    "SRPX",
    "HLA-DQB1",
    "PRSS35",
    "AEBP1",
    "SERPINE2",
    "FBLN2",
    "CD248",
    "SULF1",
    "PHGDH",
    "CDKN2A",
    "GZMA",
    "MFI2",
    "RPS4Y1",
    "SLC2A3",
    "FOS",
    "SCIN",
    "CXCL9",
    "ENPP2",
    "IFIT3",
    "SNAI2",
    "VWF",
    "ADM",
    "LEPREL1",
    "SCRG1",
    "AXL",
    "PLTP",
    "IGFBP3",
    "SBDS",
    "SOST",
    "STAT1",
    "IBSP",
    "MEPE",
    "IFITM5",
    "KSP37",
    "CDH15",
    "TMEM119",
    "SP7",
    "EFHD1",
    "CCDC3",
    "SEPP1",
    "CD36",
    "GYG2",
    "ID3",
    "FOSB",
    "SLC29A4",
    "TNFSF10",
]

if __name__ == "__main__":
    # Load in data
    expr_filename = sys.argv[1]
    clinic_filename = sys.argv[2]
    output = sys.argv[3] if sys.argv[3] != "-" else None

    sig = np.asarray(TOP_EDGES)
    expr = pd.read_csv(expr_filename).loc[:, np.asarray(TOP_NODES)]
    clinic = pd.read_csv(clinic_filename)
    clinic["mets"] = clinic["mets"].replace({"yes": 1, "no": 0})

    filter_edges = find_filter_edges(expr, sig)

    # This produces a very large dataframe
    #  we reduce it to what we need before storing it
    #  by filtering out only the edges we're interested in.
    ISNs = pd.DataFrame(
        [edge.numpy()[filter_edges] for edge in dense_isn(expr)],
        columns=sig,
        index=clinic["sample"],
    ).loc[:, sig]

    # Filtration curve
    plot_filtration_curve(
        pd.concat([ISNs, clinic.rename(index=clinic["sample"])["mets"]], axis=1),
        label_column="mets",
        output=output,
    )
