import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def analyze_network_data(data, type_analysis="Strength", abs_val=True, thr_values=None, label_column='label'):
    controls_list = {}
    cases_list = {}

    def preprocess_data(data, label_column):
        data.index.name = None

        if label_column is not None:
            data_controls = data[data[label_column] == 0]
            data_cases = data[data[label_column] == 1]

            # Drop the label column
            data_controls.drop([label_column], axis=1, inplace=True)
            data_cases.drop([label_column], axis=1, inplace=True)

            # Transpose the dataframes and reset the index
            cases = data_cases.T.reset_index()
            controls = data_controls.T.reset_index()

            # Split the values in the index column by "_"
            cases[['N1', 'N2']] = cases['index'].str.split("_", expand=True)
            cases.drop(['index'], axis=1, inplace=True)

            controls[['N1', 'N2']] = controls['index'].str.split("_", expand=True)
            controls.drop(['index'], axis=1, inplace=True)

            return controls, cases

        else:
            return data

    data = preprocess_data(data, label_column)

    def process_data(data, data_list, thr):
        for i in range(data.shape[1] - 2):
            temp = data.iloc[:, [data.shape[1] - 2, data.shape[1] - 1, i]].copy()
            if abs_val:
                temp.iloc[:, 2] = np.abs(temp.iloc[:, 2])
            aa = temp.columns[2]
            temp.columns = ["E1", "E2", "Weight"]
            mygraph = nx.from_pandas_edgelist(temp, "E1", "E2", "Weight")
            gg = nx.to_numpy_array(mygraph, weight="Weight")
            data_list[aa] = gg

    process_data(data[0], controls_list, thr_values)
    process_data(data[1], cases_list, thr_values)

    num_controls = len(controls_list)
    num_cases = len(cases_list)
    if thr_values is None:
        thr_values = np.arange(0.02, 4, 0.03)
    FC1 = np.zeros((num_controls, len(thr_values)))
    FC2 = np.zeros((num_cases, len(thr_values)))

    def calculate_FC(data_list, FC):
        for indv in range(len(data_list)):
            nm_l = list(data_list.keys())[indv]
            Adj = data_list[nm_l]
            for i in range(len(thr_values)):
                Adj_bin = np.where((Adj < thr_values[i]) & (Adj > 0), 1, 0)
                g = nx.from_numpy_array(Adj_bin, create_using=nx.Graph)
                FC[indv, i] = g.size()

    calculate_FC(controls_list, FC1)
    calculate_FC(cases_list, FC2)

    df_controls = pd.DataFrame({"Thr": thr_values, "Mean": np.mean(FC1, axis=0), "sd": np.std(FC1, axis=0), "cl": ["Controls"] * len(thr_values)})
    df_cases = pd.DataFrame({"Thr": thr_values, "Mean": np.mean(FC2, axis=0), "sd": np.std(FC2, axis=0), "cl": ["Cases"] * len(thr_values)})
    df = pd.concat([df_controls, df_cases])

    plt.figure(figsize=(12, 10))
    color_mapping = {'Cases': 'red', 'Controls': 'blue'}
    plt.errorbar(df_controls["Thr"], df_controls["Mean"], yerr=df_controls["sd"], elinewidth=0.5)
    plt.errorbar(df_cases["Thr"], df_cases["Mean"], yerr=df_cases["sd"], elinewidth=0.5, color="red")
    plt.show()
