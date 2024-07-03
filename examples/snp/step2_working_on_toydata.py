import pickle
import numpy as np
import pandas as pd

import isn_tractor.ibisn as it

# data import
snp_data = pd.read_csv("example_SNP.csv")
int_genes = pd.read_csv("example_interact_genes.csv")
with open("example_interact_snps.pkl", "rb") as file_handle:
    int_snp = pickle.load(file_handle)

# removing autocorrelations
idx_noloop = np.where(int_genes.iloc[:, 0] != int_genes.iloc[:, 1])[0]
int_snp = [int_snp[x] for x in idx_noloop]
df = int_genes.iloc[idx_noloop]

# remove a reasonable amount of interactions for reality
rows_to_remove = np.random.choice(
    df.shape[0], df.shape[0] - int(df.shape[0] * 0.1), replace=False
)
int_snp = [int_snp[x] for x in rows_to_remove]
df = df.iloc[rows_to_remove, :]

# ISNs computation
isn = it.sparse_isn(snp_data, int_snp, df, "pearson", "avg")
