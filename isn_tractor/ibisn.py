"""
Interactome based Individual Specific Networks (Ib-ISN)

Copyright 2023 Giada Lalli
"""
from typing import Union, Literal, Tuple, List, Any, Callable, Dict
from itertools import accumulate

import pandas as pd
import numpy as np
import allel
from scipy.stats import spearmanr, pearsonr
from sklearn.metrics import normalized_mutual_info_score as mutual_info
import torch as t


Metric = Union[
    Literal["pearson"],
    Literal["spearman"],
    Literal["mutual_info"],
    Literal["LD"],
    Literal["dot"],
]

Pooling = Union[Literal["max"], Literal["avg"], Literal["average"]]

# # Functions

# ## Preprocessing


def preprocess_gtf(gtf: pd.DataFrame) -> pd.DataFrame:
    """
    Ingest standardised human genome and remove unnecessary information
    such that pre-processed dataframe only contains gene name,
    chromosome, start, and stop for each feature.
    """
    gtf[["ENSEMBL_ID", "B"]] = gtf[8].str.split(";", 1, expand=True)
    gtf[["VERSION", "D"]] = gtf["B"].str.split(";", 1, expand=True)
    gtf[["NAME", "E"]] = gtf["D"].str.split(";", 1, expand=True)

    cols = [8, 10, 12, 14]
    gtf.drop(gtf.columns[cols], axis=1, inplace=True)
    gene_info: pd.DataFrame = gtf[gtf[2].str.contains("gene")]

    gene_info[["gene", "ENSEMBL_ID"]] = gtf["ENSEMBL_ID"].str.split(" ", 1, expand=True)
    gene_info[["ENSEMBL_ID", "X"]] = gtf["ENSEMBL_ID"].str.split('"', 1, expand=True)
    gene_info[["ENSEMBL_ID", "X"]] = gene_info["X"].str.split('"', 1, expand=True)

    cols = [1, 2, 5, 6, 7, 9, 10, 11, 12]
    gene_info.drop(gene_info.columns[cols], axis=1, inplace=True)
    gene_info = gene_info.rename(columns={0: "chr", 3: "start", 4: "stop"})
    gene_info = gene_info.set_index("ENSEMBL_ID")

    gene_info = gene_info[gene_info.chr != "MT"]
    gene_info = gene_info[gene_info.chr != "X"]
    gene_info = gene_info[gene_info.chr != "Y"]
    gene_info["chr"] = gene_info["chr"].astype(int)

    return gene_info


def preprocess_snp(snp_info: pd.DataFrame) -> pd.DataFrame:
    """
    Remove chromosomes that are not needed consistent with the
    preprocessing of the genome.
    """
    snp_info = snp_info.set_index("name")
    snp_info = snp_info[snp_info.chr != "23"]
    snp_info = snp_info[snp_info.chr != "25"]
    snp_info = snp_info[snp_info.chr != "26"]
    return snp_info


# ### Imputation for SNP or Gene expression dataset


def mode_genotype(column: pd.Series) -> pd.Series:
    """
    Replace missing values in a column with the mode?
    """
    mod = np.argmax(
        [
            np.sum(column == 0),
            np.sum(column == 1),
            np.sum(column == 2),
        ]
    )
    return column.replace(-9, mod)


def mean_genotype(column: pd.Series) -> pd.Series:
    """
    Replace missing values in a column with the column mean.
    """
    return column.replace(np.nan, np.nanmean(column))


def impute(
    snps: pd.DataFrame, replace: Callable[[pd.Series], Any] = mode_genotype
) -> pd.DataFrame:
    """
    Estimation of missing genotypes from the haplotype or genotype reference.

    replace: A function used to replace missing values in a column. By default,
             replacing missing data (usually stored as 9 and/or -9) with the mode
             of a column.
    """
    for j in range(snps.shape[1]):
        snp = snps.iloc[:, j]
        snps.iloc[:, j] = replace(snp)
    return snps


def impute_chunked(
    snps: pd.DataFrame, chunks: int, replace: Callable[[pd.Series], Any] = mode_genotype
) -> pd.DataFrame:
    """
    Impute a large dataset by imputing chunks of columns.
    """
    column_index = snps.columns.tolist()
    chunk_idx = np.array_split(np.arange(snps.shape[1]), chunks)
    collected = [impute(snps.iloc[:, idx], replace) for idx in chunk_idx]
    snps_imputed = pd.concat(collected, axis=1).reindex(columns=column_index)
    snps_imputed.columns = column_index
    return snps_imputed


# ## Mapping


def positional_mapping(
    snp_info: pd.DataFrame, gene_info: pd.DataFrame, neighborhood: int
) -> Dict[Any, List[Any]]:

    """
    Map SNPs to genes according to the genomic location.

    :param snp_info: a pd data.frame of size [n_snps, 2]
           where the 2 columns are the chromosome and position of every SNP.
    :param gene_info: a pd data.frame of size [n_genes, 3]
           where the 3 columns are the chromosome, start location and end
           location of every gene.
    :param neighborhood: an integer indicating how many base pairs around
           the gene are considered valid.
    :return: a dict whose keys are gene IDs and values are lists of SNP IDs
           belonging to that gene.
    """

    mapping = {}

    # loop over all genes
    for i in range(gene_info.shape[0]):
        # SNP is assigned to a gene if it's located in between the lower and upper bounds
        lowbound = gene_info.iloc[i, 1] - neighborhood
        upbound = gene_info.iloc[i, 2] + neighborhood
        idx = np.where(
            np.all(
                (
                    snp_info.to_numpy()[:, 0] == gene_info.to_numpy()[i, 0],
                    snp_info.to_numpy()[:, 1] >= lowbound,
                    snp_info.to_numpy()[:, 1] <= upbound,
                ),
                axis=0,
            )
        )[0]

        if len(idx) == 0:  # skip genes if no SNP assigned
            continue
        if len(idx) == 1:  # in case only 1 SNP is mapped to the gene
            mapping[gene_info.index.values[i]] = [snp_info.index.values[idx]]
        else:  # in case multiple SNPs are mapped to the gene
            mapping[gene_info.index.values[i]] = snp_info.index.values[idx]

    return mapping


# ## Interactions


def snp_interaction(
    interact: pd.DataFrame, gene_info: pd.DataFrame, snp_info: pd.DataFrame
) -> Tuple[List[Tuple[List[str], List[str]]], pd.Dataframe]:

    """
    Select the genes.

    :param interact: a pd data.frame of size [n_interactions, 2]
           where the 2 columns are the 2 gene IDs of the interaction.
    :param gene_info: a pd data.frame of size [n_genes, 3]
           where the 3 columns are the chromosome, start location and
           end location of every gene.
    :param snp_info: a pd data.frame of size [n_snps, 2]
           where the 2 columns are the chromosome and position
           of every SNP.
    :return:
    """

    mapping = positional_mapping(snp_info, gene_info, 2000)

    interact_sub = []
    interact_snp = []
    for gene_id_1, gene_id_2 in interact.to_records(index=False):
        if gene_id_1 in mapping and gene_id_2 in mapping:
            interact_sub.append((gene_id_1, gene_id_2))
            interact_snp.append((mapping[gene_id_1], mapping[gene_id_2]))

    return (
        interact_snp,
        pd.DataFrame(interact_sub, columns=["gene_id_1", "gene_id_2"]),
    )


# ## Metrics for SNP array


def __pooling(
    scores: np._typing._ArrayLikeFloat_co, pool: Pooling
) -> np._typing._FloatLike_co:

    """
    Pool the pairwise scores together.

    :param scores: a matrix containing all the scores.
    :param pool: a string indicating the pooling method. Currently only average- and max-pooling.
    :return: a single value.
    """

    if pool in ("avg", "average"):
        return np.mean(scores)
    if pool == "max":
        return np.max(scores)

    raise ValueError("Wrong input for pooling method!")


def __compute_metric(
    X: t.Tensor,  # pylint: disable=C0103
    Y: t.Tensor,  # pylint: disable=C0103
    method: Metric,
    pool: Pooling,
) -> np._typing._FloatLike_co:

    """
    Compute the metric between 2 sets of SNPs.

    :param X: a matrix of size [n_samples, n_snps1].
    :param Y: a matrix of size [n_samples, n_snps2].
    :param method: a string indicating the metric. Currently support Pearson correlation,
                Spearman correlation, Mutual Information and LD r^2.
    :param pool: a string indicating the pooling method. Currently only average- and max-pooling.
    :return: a single value for the metric.
    """

    if method == "pearson":  # Pearson correlation
        # pylint: disable=C0103
        XY = np.concatenate([X, Y], axis=1)
        scores = np.corrcoef(XY.T)[: X.shape[1] - 1, X.shape[1] :]
        return __pooling(scores, pool)
    if method == "spearman":  # Spearman correlation
        scores = spearmanr(X, Y)[0]
        return __pooling(scores, pool)
    if method == "mutual_info":  # normalized mutual information
        scores = np.zeros((X.shape[1], Y.shape[1]))
        for i in range(X.shape[1]):
            for j in range(Y.shape[1]):
                scores[i, j] = mutual_info(X[:, i], Y[:, j])
        return __pooling(scores, pool)
    if method == "LD":  # LD r^2 score
        scores = allel.rogers_huff_r_between(X.T, Y.T)  # LD r score
        scores = np.square(scores)  # LD r^2 score
        return __pooling(scores, pool)
    if method == "dot":  # dot product
        return __pooling(t.matmul(X.T, Y), pool)

    raise ValueError("Wrong input for metric!")


# ## Metrics for gene expression


def __compute_metric_ge(X, Y, method):

    """
    Compute the metric between 2 genes.

    :param X: a vector of size [n_samples].
    :param Y: a vector of size [n_samples].
    :param method: a string indicating the metric. Currently support Pearson correlation,
                Spearman correlation, Mutual Information and LD r^2.
    :return: a single value for the metric.
    """

    if method == "pearson":  # Pearson correlation
        score = pearsonr(X, Y)[0]
    elif method == "spearman":  # Spearman correlation
        score = spearmanr(X, Y)[0]
    elif method == "mutual_info":  # normalized mutual information
        score = mutual_info(X, Y)
    elif method == "LD":  # LD r^2 score
        score = allel.rogers_huff_r_between(X, Y)  # LD r score
        score = np.square(score)  # LD r^2 score
    else:
        raise ValueError("Wrong input for metric!")
    return score


# ## ISNs computation for SNP array


def __isn_calculation_per_edge(
    snp1: t.Tensor, snp2: t.Tensor, metric: Metric, pool: Pooling
) -> List[np._typing._FloatLike_co]:
    """
    Internal
    """
    glob = __compute_metric(snp1, snp2, metric, pool)
    snp1_acc: accumulate[  # pylint: disable=E1136
        List[np._typing._FloatLike_co]
    ] = accumulate(reversed(snp1), lambda x, y: x + [y.item()], initial=[])

    snp2_acc: accumulate[  # pylint: disable=E1136
        List[np._typing._FloatLike_co]
    ] = accumulate(reversed(snp2), lambda x, y: x + [y.item()], initial=[])

    return [
        snp1.shape[0] * (glob - avg) + avg  # type: ignore[call-overload,operator]
        for (snp1_rnge, snp2_rnge) in zip(snp1_acc, snp2_acc)
        if (
            avg := __compute_metric(
                t.tensor(snp1_rnge), t.tensor(snp2_rnge), metric, pool
            )
            or True
        )
    ][1:]


def compute_isn(
    snps: pd.DataFrame,
    interact_snp: pd.DataFrame,
    interact_gene: pd.DataFrame,
    metric: Metric,
    pool: Pooling,
) -> pd.DataFrame:
    """
    Network computation guided by weighted edges given interaction relevance.
    """
    isn = np.zeros((snps.shape[0], len(interact_snp)))

    for index, (snps_assoc_gene_1, snps_assoc_gene_2) in enumerate(interact_snp):

        element_one = np.array(snps_assoc_gene_1, dtype=object)
        element_two = np.array(snps_assoc_gene_2, dtype=object)

        intersection_1 = (
            snps[element_one[0]]
            if len(element_one) == 1
            else snps[snps.columns.intersection(element_one)]
        )

        intersection_2 = (
            snps[element_two[0]]
            if len(element_two) == 1
            else snps[snps.columns.intersection(element_two)]
        )

        isn[:, index] = __isn_calculation_per_edge(
            t.tensor(intersection_1.values),
            t.tensor(intersection_2.values),
            metric,
            pool,
        )

    return pd.DataFrame(isn, columns=[a + "_" + b for a, b in interact_gene.values])


# ## ISNs computation for gene expression
def __isn_computation_per_edge(vector1, vector2, metric):
    """
    Internal
    """

    glob = __compute_metric_ge(vector1, vector2, metric)
    result = []

    for indx in range(vector1.shape[0]):
        gene1_LOO = np.delete(vector1, indx, axis=0)
        gene2_LOO = np.delete(vector2, indx, axis=0)
        avg = __compute_metric_ge(gene1_LOO, gene2_LOO, metric)
        result.append(vector1.shape[0] * (glob - avg) + avg)

    return result


def isn_calculation_all(df, interact, metric):
    import numpy as np
    import pandas as pd

    isn = np.zeros((df.shape[0], len(interact)))

    for index, tuple in enumerate(interact.values):
        if not np.all(interact.iloc[index].isin(df.columns)):
            continue

        element_one = np.array(tuple[0], dtype=object)
        element_two = np.array(tuple[1], dtype=object)

        x = df[element_one]
        y = df[element_two]

        edge = __isn_computation_per_edge(
            t.tensor(x.values), t.tensor(y.values), metric
        )
        isn[:, index] = edge

        print("Edge:", index, "/", len(interact))

    isn = pd.DataFrame(isn, columns=[a + "_" + b for a, b in interact.values])
    isn = isn.iloc[:, np.where(isn.sum() != 0)[0]]
    return isn
