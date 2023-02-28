"""
Interactome based Individual Specific Networks (Ib-ISN)

Copyright 2023 Giada Lalli
"""
from typing import Union, Literal, Tuple, List, Any, Callable, Optional
import pandas as pd
import numpy as np
from numpy._typing import _ArrayLikeFloat_co, _FloatLike_co
from scipy.stats import pearsonr, spearmanr
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

GeneInteraction = Tuple[List[str], List[str]]


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
    gene_info = gtf[gtf[2].str.contains("gene")]

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
):
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
) -> Tuple[List[GeneInteraction], pd.DataFrame]:
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

    interact_gene = []
    interact_snp = []
    for gene_id_1, gene_id_2 in interact.to_records(index=False):
        if gene_id_1 in mapping and gene_id_2 in mapping:
            interact_gene.append((gene_id_1, gene_id_2))
            interact_snp.append((mapping[gene_id_1], mapping[gene_id_2]))

    return (
        interact_snp,
        pd.DataFrame(interact_gene, columns=["gene_id_1", "gene_id_2"]),
    )


# ## Metrics for SNP array


def __pearson_metric(first, second):
    if (first.dim(), second.dim()) == (1, 1):
        return pearsonr(first, second).statistic

    combined = np.concatenate([first, second], axis=1)
    return np.corrcoef(combined.T)[: first.shape[1] - 1, first.shape[1] :]


def __spearman_metric(first, second):
    return spearmanr(first, second).statistic


def __mutual_info_metric(first, second):
    if (first.dim(), second.dim()) == (1, 1):
        return mutual_info(first, second)

    scores = np.zeros((first.shape[1], second.shape[1]))
    for i in range(first.shape[1]):
        for j in range(second.shape[1]):
            scores[i, j] = mutual_info(first[:, i], second[:, j])
    return scores


def __dot_metric(first, second):
    return t.matmul(first.permute(*t.arange(first.ndim - 1, -1, -1)), second).numpy()


# ## ISNs computation for SNP array


def __isn_calculation_per_edge(
    snp1_list,
    snp2_list,
    metric,
    pool: Callable[
        [Union[_ArrayLikeFloat_co, _FloatLike_co]],
        _FloatLike_co,
    ],
):
    """
    Internal
    """
    glob = pool(metric(snp1_list, snp2_list))
    result = []

    for indx in range(snp1_list.shape[0]):
        snp1_loo = np.delete(snp1_list, indx, axis=0)
        snp2_loo = np.delete(snp2_list, indx, axis=0)
        avg = pool(metric(snp1_loo, snp2_loo))
        # type: ignore[call-overload,operator]
        result.append(snp1_list.shape[0] * (glob - avg) + avg)

    return result


def __make_array(*xs):
    return np.array(xs, dtype=object)


def __identity(value: _FloatLike_co) -> _FloatLike_co:
    return value


def isn(
    data,
    interact_snp,
    interact_gene,
    metric: Union[
        Literal["pearson"],
        Literal["spearman"],
        Literal["mutual_info"],
        Literal["dot"],
        Callable[
            [t.Tensor, t.Tensor],
            Union[_ArrayLikeFloat_co, _FloatLike_co],
        ],
    ],
    pool: Optional[
        Union[
            Literal["max"],
            Literal["avg"],
            Literal["average"],
            Callable[[_ArrayLikeFloat_co], _FloatLike_co],
        ]
    ] = None,
):
    """
    Network computation guided by weighted edges given interaction relevance.
    """
    if metric not in ["pearson", "spearman", "mutual_info", "dot"]:
        raise ValueError(f'"{metric}" is not a valid metric')
    if pool is not None and pool not in ["max", "avg", "average"]:
        raise ValueError(f'"{pool}" is not a valid pooling method')

    if isinstance(metric, str):
        metric_fn = {
            "pearson": __pearson_metric,
            "spearman": __spearman_metric,
            "mutual_info": __mutual_info_metric,
            "dot": __dot_metric,
        }.get(metric)
    else:
        metric_fn = metric

    if pool is None:
        pooling_fn = __identity
    elif isinstance(pool, str):
        pooling_fn = {
            "max": np.max,
            "avg": np.mean,
            "average": np.mean,
        }.get(pool)
    else:
        pooling_fn = pool

    if interact_snp is not None:
        interact = interact_snp
    else:
        interact = interact_gene.values
    network = np.zeros((data.shape[0], len(interact)))
    assert np.all(snp.isin(data.columns) for snp in interact)
    assert metric_fn is not None
    assert pooling_fn is not None

    for index, (assoc_gene_1, assoc_gene_2) in enumerate(interact):
        element_one = __make_array(assoc_gene_1)
        element_two = __make_array(assoc_gene_2)

        intersection_1 = (
            data[element_one[0]]
            if len(element_one) == 1
            else data[data.columns.intersection(element_one)]
        )

        intersection_2 = (
            data[element_two[0]]
            if len(element_two) == 1
            else data[data.columns.intersection(element_two)]
        )

        network[:, index] = __isn_calculation_per_edge(
            t.tensor(intersection_1.values),
            t.tensor(intersection_2.values),
            metric_fn,
            pooling_fn,
        )

    return pd.DataFrame(network, columns=[a + "_" + b for a, b in interact_gene.values])
