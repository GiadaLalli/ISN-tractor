#!/usr/bin/env python
# coding: utf-8

# # Import Libraries

import pandas as pd
import numpy as np
import sys
import allel
from scipy.stats import spearmanr
from sklearn.metrics import normalized_mutual_info_score as mutual_info
import torch as t

#data managing
import pickle
import marshal

# # Data Upload

# snp dset
df = pd.read_csv(filename)

#snp info: name, chr, position
snp_info = pd.read_csv(filename)

#tuple: interactome interactions
interact = pd.read_csv(filename) 

#list of genes in the human genome with chr:start-stop
gtf = pd.read_csv(filename)

# # Functions

# ## Preprocessing

def preprocess_gtf(gtf):

    gtf[['ENSEMBL_ID', 'B']] = gtf[8].str.split(';', 1, expand=True)
    gtf[['VERSION', 'D']] = gtf['B'].str.split(';', 1, expand=True)
    gtf[['NAME', 'E']] = gtf['D'].str.split(';', 1, expand=True)

    cols = [8, 10, 12, 14]
    gtf.drop(gtf.columns[cols],axis=1,inplace=True)
    gene_info = gtf[gtf[2].str.contains('gene')]

    gene_info[['gene', 'ENSEMBL_ID']] = gtf['ENSEMBL_ID'].str.split(' ', 1, expand=True)
    gene_info[['ENSEMBL_ID', 'X']] = gtf['ENSEMBL_ID'].str.split('"', 1, expand=True)
    gene_info[['ENSEMBL_ID', 'X']] = gene_info['X'].str.split('"', 1, expand=True)

    cols = [1, 2, 5, 6, 7, 9, 10, 11, 12]
    gene_info.drop(gene_info.columns[cols],axis=1,inplace=True)
    gene_info = gene_info.rename(columns={0: "chr", 3: "start", 4: "stop"})
    gene_info = gene_info.set_index('ENSEMBL_ID')
    
    gene_info = gene_info[gene_info.chr != 'MT']
    gene_info = gene_info[gene_info.chr != 'X']
    gene_info = gene_info[gene_info.chr != 'Y']
    gene_info['chr'] = gene_info['chr'].astype(int)

    return(gene_info)

def preprocess_snp(snp_info):
    snp_info = snp_info.set_index('name')
    snp_info = snp_info[snp_info.chr != '23']
    snp_info = snp_info[snp_info.chr != '25']
    snp_info = snp_info[snp_info.chr != '26']
    return(snp_info)

# ### Imputation 

def impute(snps):
    for j in range(snps.shape[1]):
        snp = snps.iloc[:, j]
        miss = snp == -9
        if np.sum(miss) == 0:
            continue
        n_0 = np.sum(snp == 0)
        n_1 = np.sum(snp == 1)
        n_2 = np.sum(snp == 2)
        # compute the mode genotype of every SNP
        mod = np.argmax([n_0, n_1, n_2])
        snps.iloc[miss, j] = mod
    return snps

def impute_chunked(snps, chunks):
    column_index = snps.columns.tolist()
    chunk_idx = np.array_split(np.arange(snps.shape[1]), chunks)
    collected = [impute(snps.iloc[:, idx]) for idx in chunk_idx]
    df = pd.concat(collected, axis=1)
    df = df.reindex(columns=column_index)
    df.columns = column_index
    return df

# ## Mapping

def positional_mapping(snp_info, gene_info, neighborhood):
    
    """
    Map SNPs to genes according to the genomic location.

    :param snp_info: a pd data.frame of size [n_snps, 2]
                 where the 2 columns are the chromosome and position of every SNP.
    :param gene_info: a pd data.frame of size [n_genes, 3]
                  where the 3 columns are the chromosome, start location and end location of every gene.
    :param neighborhood: an integer indicating how many base pairs around the gene are considered valid.
    :return: a dict whose keys are gene IDs and values are lists of SNP IDs belonging to that gene.
    """
    
    mapping = {}

    # loop over all genes
    for i in range(gene_info.shape[0]):
        # SNP is assigned to a gene if it's located in between the lower and upper bounds
        lowbound = gene_info.iloc[i, 1] - neighborhood
        upbound = gene_info.iloc[i, 2] + neighborhood
        idx = np.where(np.all((snp_info.to_numpy()[:,0] == gene_info.to_numpy()[i,0],
            snp_info.to_numpy()[:,1] >= lowbound, snp_info.to_numpy()[:,1] <= upbound), axis = 0))[0]
        

        if len(idx) == 0: #skip genes if no SNP assigned
            continue
        elif len(idx) == 1: # in case only 1 SNP is mapped to the gene
            mapping[gene_info.index.values[i]] = [snp_info.index.values[idx]]
        else: # in case multiple SNPs are mapped to the gene
            mapping[gene_info.index.values[i]] = snp_info.index.values[idx]
    
    return(mapping)

# ## Interactions

def snp_interaction(interact, gene_info, snp_info):
    
    """
    Select the genes.

    :param interact: a pd data.frame of size [n_interactions, 2]
                 where the 2 columns are the 2 gene IDs of the interaction.
    :param gene_info: a pd data.frame of size [n_genes, 3]
                  where the 3 columns are the chromosome, start location and end location of every gene.
    :param snp_info: a pd data.frame of size [n_snps, 2]
                 where the 2 columns are the chromosome and position of every SNP.
    :return: a list of tuples whose elements are 2 lists.
    """

    mapping = positional_mapping(snp_info, gene_info, 2000)

    interact_sub = []
    interact_snp = []
    interact = interact.to_records(index=False)
    for a, b in interact:
        if a in mapping.keys() and b in mapping.keys():
            interact_sub.append([a, b])
            interact_snp.append((mapping[a], mapping[b]))

    interact_sub = pd.DataFrame(interact_sub, columns=['gene1', 'gene2'])
  
    return(interact_snp, interact_sub)

# ## Metrics

def pooling(scores, pool):
    
    """
    Pool the pairwise scores together.

    :param scores: a matrix containing all the scores.
    :param pool: a string indicating the pooling method. Currently only average- and max-pooling.
    :return: a single value.
    """
    
    if pool == 'average':
        return np.mean(scores)
    elif pool == 'max':
        return np.max(scores)
    #let's do error handling instead of sys.exit - raise error instead
    else:
        #sys.exit('Wrong input for pooling method!')
        raise ValueError('Wrong input for pooling method!')

def compute_metric(X, Y, method, pool):
    
    """
    Compute the metric between 2 sets of SNPs.

    :param X: a matrix of size [n_samples, n_snps1].
    :param Y: a matrix of size [n_samples, n_snps2].
    :param method: a string indicating the metric. Currently support Pearson correlation, 
                Spearman correlation, Mutual Information and LD r^2.
    :param pool: a string indicating the pooling method. Currently only average- and max-pooling.
    :return: a single value for the metric.
    """
    
    if method == "pearson": # Pearson correlation
        XY = np.concatenate([X, Y], axis = 1)
        scores = np.corrcoef(XY.T)[:X.shape[1]-1, X.shape[1]:]
        score = pooling(scores, pool)
    elif method == "spearman": # Spearman correlation
        scores = spearmanr(X, Y)[0]
        score = pooling(scores, pool)
    elif method == "mutual_info": # normalized mutual information
        scores = np.zeros((X.shape[1], Y.shape[1]))
        for i in range(X.shape[1]):
            for j in range(Y.shape[1]):
              scores[i,j] = mutual_info(X[:,i], Y[:,j])
        score = pooling(scores, pool)
    elif method == "LD": # LD r^2 score
        scores = allel.rogers_huff_r_between(X.T, Y.T) # LD r score
        scores = np.square(scores) # LD r^2 score
        score = pooling(scores, pool)
        #let's do error handling instead of sys.exit - raise error instead
    else:
        #sys.exit('Wrong input for metric!')
        raise ValueError('Wrong input for metric!')
    return score

# ## ISNs calculation

def isn_calculation_all(df, interact_snp, interact_gene, metric, pool):
    import numpy as np
    import pandas as pd

    isn = np.zeros((df.shape[0], len(interact_snp)))

    for index, tuple in enumerate(interact_snp):

        element_one = np.array(tuple[0], dtype=object)
        element_two = np.array(tuple[1], dtype=object)

        if len(element_one) == 1:
            x = df[element_one[0]]
        else:
            x = df[df.columns.intersection(element_one)]
        if len(element_two) == 1:
            y = df[element_two[0]]
        else:
            y = df[df.columns.intersection(element_two)]

        edge = isn_calculation_per_edge(t.tensor(x.values), t.tensor(y.values), metric, pool)
        isn[:, index] = edge

        print("Edge:", index, "/", len(interact_snp))
    
    isn = pd.DataFrame(isn, columns=[a+'_'+b for a,b in interact_gene.values])
    return(isn)

# ## Data calling

gene_info = preprocess_gtf(gtf)

snp_info = preprocess_snp(snp_info)

df = impute(df)

tmp = positional_mapping(snp_info, gene_info, neighborhood=0)

interact_snp, interact_sub = snp_interaction(interact, gene_info, snp_info)

df_isn = isn_calculation_all(df, interact_snp, interact_sub, 'spearman', 'max')
