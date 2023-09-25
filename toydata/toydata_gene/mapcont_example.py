"""
This toy example demonstrates how to work with mapped continuous data.

The dataset was artificially generated to resemble realistic gene expression
data by utilizing the actual Human Genome Assembly (GRCh38 version p.13) and
the real Interactome (HuRI, by Luck et al., 2020); ensembl_ids were associated
to the genes through BioMart.
The imputation process was performed prior to the computation of both
sparse and dense version of ISNs.
"""

from pathlib import Path
import urllib.request as req

import pandas as pd
import numpy as np

import isn_tractor.ibisn as it


# data import

# HuRI
interact = pd.read_csv("HuRI.tsv", delimiter="\t", engine="python", header=None)
# HumanGenome - GRCh38 version p.13
gtf_path = Path("Homo_sapiens.GRCh38.105.chr.gtf.gz")
if not gtf_path.exists():
    with req.urlopen(
        "https://ftp.ensembl.org/pub/release-105/gtf/homo_sapiens/Homo_sapiens.GRCh38.105.chr.gtf.gz"
    ) as response:
        gtf_path.write_bytes(response.read())

gtf = pd.read_csv(
    "Homo_sapiens.GRCh38.105.chr.gtf.gz",
    delimiter="\t",
    engine="python",
    header=None,
    compression="gzip",
    skiprows=5,
)
# HumanGenome Preprocessing
gtf = it.preprocess_gtf(gtf)
# ENSEMBL_id
index_list = gtf.index.tolist()

# extracted ALL the ensembl_ids from the GRCh38, processed on Biomart to get
# the needed info
corr = pd.read_csv("corr_genename_ensid.txt", delimiter=",", engine="python")
corr = corr.dropna(subset=["Gene name"])
corr = corr[corr["Gene stable ID"].isin(index_list)]
corr = corr.drop_duplicates(subset="Gene stable ID", keep=False)

# Data creation:

# create random sampleXgene dataset with 200 rows and 1000 columns of random
# floating values in range
np.random.seed(123)
df2 = pd.DataFrame(np.random.uniform(-50, +50, (200, 1000)))

# Define a list of convenient names from real case scenario
names = corr["Gene stable ID"].tolist()

# Assign random names from the list to the columns of the dataframe
df2.columns = np.random.choice(names, size=df2.shape[1], replace=False)

# Add some NaN for reality
nan_indices = np.random.choice(df2.size, size=500, replace=False)
df2.values.ravel()[nan_indices] = np.nan


# save toydata generated as above
# df2.to_csv(r'toydata_X.csv', sep=',', index = False)

# process the newly created df to remove NaN
imputed = it.impute(df2, replace=it.mean_genotype)
# simulated interactions for dense network
genes = imputed.columns

interact = []
for i in range(len(genes)):
    for j in range(i + 1, len(genes)):
        interact.append((genes[i], genes[j]))

interact = pd.DataFrame(interact, columns=["gene1", "gene2"])


# computation of sparse isn
s_isn = it.sparse_isn(
    df2, interact_unmapped=None, interact_mapped=interact, metric="pearson", pool=None
)
# computation of dense isn
d_isn = it.dense_isn(df2, metric="pearson")
