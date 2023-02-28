#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import libraries
import pandas as pd
import numpy as np
import sys
import allel
from scipy.stats import spearmanr, pearsonr
from sklearn.metrics import normalized_mutual_info_score as mutual_info
import torch as t
import isn_tractor.ibisn as it
import random
import time

#data managing
import pickle
import marshal


# In[2]:


#data import 

#HuRI 
interact = pd.read_csv('/massstorage/URT/GEN/BIO3/PRIV/Projects/isnData/HuRI.tsv', delimiter="\t", engine='python', header=None) 
#HumanGenome - GRCh38 version p.13
gtf = pd.read_csv('/massstorage/URT/GEN/BIO3/PRIV/Projects/isnData/Homo_sapiens.GRCh38.105.chr.gtf', delimiter="\t", engine='python', header=None)
#HumanGenome Preprocessing 
gtf = it.preprocess_gtf(gtf)
#ENSEMBL_id 
index_list = gtf.index.tolist()


# In[3]:


#extracted ALL the ensembl_ids from the GRCh38, processed on Biomart to get the needed info
corr = pd.read_csv('/massstorage/URT/GEN/BIO3/PRIV/Team/Giada/isn/corr_genename_ensid.txt', delimiter=",", engine='python')
corr = corr.dropna(subset=['Gene name'])
corr = corr[corr['Gene stable ID'].isin(index_list)]
corr = corr.drop_duplicates(subset='Gene stable ID', keep=False)
corr


# In[12]:


#create random geneXsample dataset with 200 rows and 1000 columns of random floating values [0 : 1]
np.random.seed(123)
df2 = pd.DataFrame(np.random.rand(200, 1000))

# Define a list of random names
names = corr['Gene stable ID'].tolist()

# Assign random names from the list to the first column of the dataframe
df2.columns = random.choices(names, k=df2.shape[1])

# Add some NaN
nan_indices = np.random.choice(df2.size, size=500, replace=False)
df2.values.ravel()[nan_indices] = np.nan

# View the first few rows of the dataframe
df2


# In[34]:


#save toydata generated as above
#df2.to_csv(r'/massstorage/URT/GEN/BIO3/PRIV/Team/Giada/isn/toydata_gene.csv', sep=',', index = False)


# In[13]:


imputed = impute(df2)


# ### functions 

# In[5]:


def impute(gene_df):
    for j in range(gene_df.shape[1]):
        gene = gene_df.iloc[:, j]
        miss = np.isnan(gene)
        if np.sum(miss) == 0:
            continue
        # compute the mode genotype of every SNP
        mod = np.nanmean(gene)
        gene_df.iloc[miss, j] = mod
    return gene_df


# In[6]:


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


# In[7]:


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


# In[19]:


st = time.process_time()
isn = isn_calculation_all(imputed, interact, 'pearson')
elapsed_time = time.process_time() - st
print('CPU Execution time', elapsed_time, 'seconds')


# In[ ]:




