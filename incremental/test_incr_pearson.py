import pytest
from isn_tractor.ibisn import sparse_isn, dense_isn, __spearman_metric

from numpy import array, zeros, concatenate, corrcoef, int64, float32
import pandas as pd
from pandas.testing import assert_frame_equal


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

def test_dense_incr_pears():
    data = pd.DataFrame(
        [(0.162634, 0.449745, 0.968108), (0.409558, 0.092939, 0.284362), (0.755906, 0.189236, 0.774311)], 
    columns=["gene1", "gene2", "gene3"]
    )
    assert_frame_equal(
        dense_isn(data.T, "pearson"),
        pd.DataFrame(
            [
                ("gene1", "gene1", 1.000000, 1.000000, 1.000000),
                ("gene1", "gene2", -3.902325, 0.097675, 0.097675),
                ("gene1", "gene3", -2.543286, 1.456714, 1.456714),
                ("gene2", "gene1", -3.902325, 0.097675, 0.097675),
                ("gene2", "gene2", 1.000000, 1.000000, 1.000000),
                ("gene2", "gene3", 0.625879, 0.625879, 0.625879),
                ("gene3", "gene1", -2.543286, 1.456714, 1.456714),
                ("gene3", "gene2", 0.625879, 0.625879, 0.625879),
                ("gene3", "gene3", 1.000000, 1.000000, 1.000000),
            ],
            columns=["reg", "tar", "0", "1", "2"],
        ),
    )
