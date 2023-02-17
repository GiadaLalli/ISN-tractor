#import libraries
import pandas as pd
import numpy as np
import sys
import torch as t
import isn_tractor.ibisn as it
import random

from scipy.stats import spearmanr, pearsonr
from sklearn.metrics import normalized_mutual_info_score as mutual_info

#data import
df = pd.read_csv('toydata')
interact = pd.read_csv('HuRI')

#functions

# imputation
def impute(gene_df):
    for j in range(gene_df.shape[1]):
        gene = gene_df.iloc[:, j]
        miss = np.isnan(gene)
        if np.sum(miss) == 0:
            continue
        # compute the mean genotype of every SNP
        media = np.nanmean(gene)
        gene_df.iloc[miss, j] = media
    return gene_df

#metrics 
def compute_metric(X, Y, method):
    
    """
    Compute the metric between 2 genes.

    :param X: a vector of size [n_samples].
    :param Y: a vector of size [n_samples].
    :param method: a string indicating the metric. Currently support Pearson correlation, 
                Spearman correlation, Mutual Information and LD r^2.
    :return: a single value for the metric.
    """
    
    if method == "pearson": # Pearson correlation
        score = pearsonr(X, Y)[0]
    elif method == "spearman": # Spearman correlation
        score = spearmanr(X, Y)[0]
    elif method == "mutual_info": # normalized mutual information
        score = mutual_info(X, Y)
    elif method == "LD": # LD r^2 score
        score = allel.rogers_huff_r_between(X, Y) # LD r score
        score = np.square(score) # LD r^2 score
    else:
        raise ValueError('Wrong input for metric!')
    return score

#ISN computation
def isn_calculation_per_edge(vector1, vector2, metric):

    glob = compute_metric(vector1, vector2, metric)
    result = []

    for indx in range(vector1.shape[0]):
        gene1_LOO = np.delete(vector1, indx, axis = 0)
        gene2_LOO = np.delete(vector2, indx, axis = 0)
        avg = compute_metric(gene1_LOO, gene2_LOO, metric)
        result.append(vector1.shape[0]*(glob - avg) + avg )

    return(result)

def isn_calculation_all(df, interact, metric):
    import numpy as np
    import pandas as pd

    isn = np.zeros((df.shape[0], len(interact)))

    for index, tuple in enumerate(interact.values):
        if not np.all(interact.iloc[index].isin(df.columns)): continue

        element_one = np.array(tuple[0], dtype=object)
        element_two = np.array(tuple[1], dtype=object)
        
        x = df[element_one]
        y = df[element_two]
    
        edge = isn_calculation_per_edge(t.tensor(x.values), t.tensor(y.values), metric)
        isn[:, index] = edge

        print("Edge:", index, "/", len(interact))
    
    isn = pd.DataFrame(isn, columns=[a+'_'+b for a,b in interact.values])
    isn = isn.iloc[:, np.where(isn.sum() != 0)[0]]
    return(isn)

#preprocessing 
imputed = impute(df)

#ISN computation 
isn = isn_calculation_all(imputed, interact, metric)


