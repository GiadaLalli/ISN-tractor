'''
TBM: from Numpy to Torch 
also the resulting df must be reshaped - look into ibisn.py/dense_isn
and make the format == to the resulting df from ibisn.py/sparse_isn
(nda: no more "reg" and "tar" as edge_names)
'''


import numpy as np
import pandas as pd

def incremental_pearson(data):
    """
    Compute the cross-correlation matrix of the input data frame A.
    
    Parameters:
        data (pandas.DataFrame): Input data frame of size (N, M) containing the data to compute cross-correlation matrix.
        
    Returns:
        pandas.DataFrame: Cross-correlation matrix of the input data frame data.
    """
    N = data.shape[0]
    dot_prod = np.dot(data.T, data)
    mean_vect = np.sum(data, axis=0)
    std_vect = np.sum(data**2, axis=0)
    glob_net = np.corrcoef(data.T)
    df = pd.DataFrame(
        np.nan,
        index=np.arange(data.shape[1] * data.shape[1]),
        columns=["reg", "tar"] + list(data.index),
    ).astype(object)
    df.iloc[:, 0] = np.repeat(data.columns.values, data.shape[1])
    df.iloc[:, 1] = np.tile(data.columns.values, data.shape[1])
    
    for i in range(data.shape[0]):
        Sq = np.outer(data.iloc[i,:],data.iloc[i,:])
        Cq = np.outer(mean_vect-data.iloc[i,:],mean_vect-data.iloc[i,:])
        Dq = np.sqrt((N-1)*(std_vect - data.iloc[i,:]**2)-(mean_vect-data.iloc[i,:])**2)
        nom = (N-1)*(S-Sq)-Cq
        den = (np.outer(Dq.T, Dq))
        result = (nom/den)
        final_result = (N*glob_net)-((N-1)*result)
        df.iloc[:, i + 2] = final_result.flatten()
        
    return df
