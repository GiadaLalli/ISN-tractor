# import libraries
import numpy as np
import isn_tractor.ibisn as it
import pickle
import pandas as pd

# data import
snp_data = pd.read_csv("toydata_SNP.csv")
int_genes = pd.read_csv("toydata_interact_genes.csv")
with open("toydata_interact_snps.pkl", "rb") as file_handle:
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
