"""
Interactome based Individual Specific Networks (Ib-ISN)

Copyright 2023 Giada Lalli
"""
from typing import Union, Literal, Tuple, List, Any, Callable, Optional
import pandas as pd
import numpy as np
from numpy._typing import _ArrayLikeFloat_co, _FloatLike_co
import torch as t

MetricFn = Callable[
    [t.Tensor, t.Tensor],
    Union[_ArrayLikeFloat_co, _FloatLike_co],
]

PoolingFn = Callable[
    [Union[_ArrayLikeFloat_co, _FloatLike_co]],
    _FloatLike_co,
]

Metric = Union[
    Literal["pearson"],
    Literal["incremental_pearson"],
    Literal["spearman"],
    Literal["dot"],
    MetricFn,
]

Pooling = Union[Literal["max"], Literal["avg"], Literal["average"], PoolingFn]

MappedInteraction = Tuple[List[str], List[str]]


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
    Replace missing values in a column with the mode
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
    data: pd.DataFrame, replace: Callable[[pd.Series], Any] = mode_genotype
) -> pd.DataFrame:
    """
    Estimation of missing genotypes from the haplotype or genotype reference.

    replace: A function used to replace missing values in a column. By default,
             replacing missing data (usually stored as 9 and/or -9) with the mode
             of a column. You can use the supplied `mean_genotype` function for
             continuous data or `mode_genotype` for discrete data.
    """
    for j in range(data.shape[1]):
        datum = data.iloc[:, j]
        data.iloc[:, j] = replace(datum)
    return data


def impute_chunked(
    data: pd.DataFrame, chunks: int, replace: Callable[[pd.Series], Any] = mode_genotype
) -> pd.DataFrame:
    """
    Impute a large dataset by imputing chunks of columns.
    """
    columns = data.columns.tolist()
    chunk_idx = np.array_split(np.arange(data.shape[1]), chunks)
    collected = [impute(data.iloc[:, idx], replace) for idx in chunk_idx]
    imputed = pd.concat(collected, axis=1).reindex(columns=columns)
    imputed.columns = columns
    return imputed


# ## Mapping


def positional_mapping(
    unmapped_info: pd.DataFrame, mapped_info: pd.DataFrame, neighborhood: int
):
    """
    Map SNPs to genes according to the genomic location.

    :param unmapped_info: a pd data.frame of size [n_snps, 2]
           where the 2 columns are the chromosome and position of every SNP.
    :param mapped_info: a pd data.frame of size [n_genes, 3]
           where the 3 columns are the chromosome, start location and end
           location of every gene.
    :param neighborhood: an integer indicating how many base pairs around
           the gene are considered valid.
    :return: a dict whose keys are gene IDs and values are lists of SNP IDs
           belonging to that gene.
    """

    mapping = {}

    # loop over all genes
    for i in range(mapped_info.shape[0]):
        # SNP is assigned to a gene if it's located in between the lower and upper bounds
        lowbound = mapped_info.iloc[i, 1] - neighborhood
        upbound = mapped_info.iloc[i, 2] + neighborhood
        idx = np.where(
            np.all(
                (
                    unmapped_info.to_numpy()[:, 0] == mapped_info.to_numpy()[i, 0],
                    unmapped_info.to_numpy()[:, 1] >= lowbound,
                    unmapped_info.to_numpy()[:, 1] <= upbound,
                ),
                axis=0,
            )
        )[0]

        if len(idx) == 0:  # skip genes if no SNP assigned
            continue
        if len(idx) == 1:  # in case only 1 SNP is mapped to the gene
            mapping[mapped_info.index.values[i]] = [unmapped_info.index.values[idx]]
        else:  # in case multiple SNPs are mapped to the gene
            mapping[mapped_info.index.values[i]] = unmapped_info.index.values[idx]

    return mapping


# ## Interactions


def map_interaction(
    interact: pd.DataFrame,
    mapped_info: pd.DataFrame,
    unmapped_info: pd.DataFrame,
    neighborhood: int = 2000,
) -> Tuple[List[MappedInteraction], pd.DataFrame]:
    """
    Select the genes.

    :param interact: a pd data.frame of size [n_interactions, 2]
           where the 2 columns are the 2 gene IDs of the interaction.
    :param mapped_info: a pd data.frame of size [n_genes, 3]
           where the 3 columns are the chromosome, start location and
           end location of every gene.
    :param unmapped_info: a pd data.frame of size [n_snps, 2]
           where the 2 columns are the chromosome and position
           of every SNP.
    :return:
    """

    mapping = positional_mapping(unmapped_info, mapped_info, neighborhood)

    interact_mapped = []
    interact_unmapped = []
    for feature_1, feature_2 in interact.to_records(index=False):
        if feature_1 in mapping and feature_2 in mapping:
            interact_mapped.append((feature_1, feature_2))
            interact_unmapped.append((mapping[feature_1], mapping[feature_2]))

    return (
        interact_unmapped,
        pd.DataFrame(interact_mapped, columns=["gene_id_1", "gene_id_2"]),
    )


# ## Metrics for **unmapped discrete data


def __pearson_metric(first: t.Tensor, second: t.Tensor) -> t.Tensor:
    if first.dim() == 1 and second.dim() == 1:
        combined = t.stack([first, second], dim=1)
        return t.corrcoef(combined.T)[0, 1]

    combined = t.cat([first, second], dim=1)
    return t.corrcoef(combined.T)[: first.shape[1], first.shape[1]]


def __spearman_metric(first, second):
    if first.ndim == 1 and second.ndim == 1:
        data = t.stack((first, second), dim=1)
        for i in range(data.shape[1]):
            _, inv, counts = t.unique(
                data[:, i], return_inverse=True, return_counts=True
            )
            csum = t.zeros_like(counts)
            csum[1:] = counts[:-1].cumsum(dim=-1)
            data[:, i] = csum[inv]
        corr = t.corrcoef(data.T)[0, 1]
    else:
        data = t.cat((first, second), dim=1)
        for i in range(data.shape[1]):
            _, inv, counts = t.unique(
                data[:, i], return_inverse=True, return_counts=True
            )
            csum = t.zeros_like(counts)
            csum[1:] = counts[:-1].cumsum(dim=-1)
            data[:, i] = csum[inv]
        corr = t.corrcoef(data.T)[: first.shape[1], first.shape[1] :]
    return corr


def __dot_metric(first, second):
    dot_prod = t.matmul(first.permute(*t.arange(first.ndim - 1, -1, -1)), second)
    return dot_prod.float()


# ## ISNs computation for SNP array


def __isn_edge(
    metric: MetricFn,
    pool: PoolingFn,
):
    """
    Internal
    """

    def isn_edge_implementation(first: t.Tensor, second: t.Tensor):
        rows = first.shape[0]
        glob = pool(metric(first, second))
        result = []

        for indx in range(first.shape[0]):
            loo_1 = t.cat((first[:indx], first[indx + 1 :]))
            loo_2 = t.cat((second[:indx], second[indx + 1 :]))
            avg = pool(metric(loo_1, loo_2))
            result.append(rows * (glob - avg) + avg)  # type: ignore[call-overload,operator]

        return np.array(result, dtype=np.float64)

    return isn_edge_implementation


def __make_array(*xs):
    return np.array(xs, dtype=object)


def __make_edge_fn(
    data,
    metric_fn: MetricFn,
    pool_fn: PoolingFn,
    device: Optional[t.device] = None,
):
    edge = __isn_edge(metric_fn, pool_fn)

    def make_edge(assoc_1, assoc_2):
        element_one = __make_array(assoc_1)
        element_two = __make_array(assoc_2)

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

        return edge(
            t.tensor(intersection_1.values, device=device),
            t.tensor(intersection_2.values, device=device),
        )

    return make_edge


def __identity(value: _FloatLike_co) -> _FloatLike_co:
    return value


# pylint: disable=too-many-arguments
def sparse_isn(
    data,
    interact_unmapped,
    interact_mapped,
    metric: Metric,
    pool: Optional[Pooling] = None,
    device: Optional[t.device] = None,
):
    """
    Network computation guided by weighted edges given interaction relevance.

    Specify the pyTorch device on which computation should take place. For example, pass:
    `device=t.device("cuda")` to run on the 'current' CUDA device.
    """
    if interact_unmapped is not None:
        interact = interact_unmapped
    else:
        interact = interact_mapped.values
    assert np.all(snp.isin(data.columns) for snp in interact)  # type: ignore[call-overload]
    if metric == "incremental_pearson" and interact_unmapped is None:
        return dense_isn(data, device)

    if isinstance(metric, str):
        if (
            metric_fn := {
                "pearson": __pearson_metric,
                "spearman": __spearman_metric,
                "dot": __dot_metric,
            }.get(metric)
        ) is None:
            raise ValueError(f'"{metric}" is not a valid metric')
    else:
        metric_fn = metric

    if pool is None:
        pooling_fn: PoolingFn = __identity  # type: ignore[assignment]
    elif isinstance(pool, str):
        if (
            pooling_fn := {  # type: ignore[assignment]
                "max": t.max,
                "avg": t.mean,
                "average": t.mean,
            }.get(pool)
        ) is None:
            raise ValueError(f'"{pool}" is not a valid pooling method')
    else:
        pooling_fn = pool

    assert metric_fn is not None
    assert pooling_fn is not None

    isn_edge = __make_edge_fn(data, metric_fn, pooling_fn, device=device)

    return pd.DataFrame(
        np.column_stack([isn_edge(*assoc) for assoc in interact]),
        columns=[a + "_" + b for a, b in interact_mapped.values],
    )


def dense_isn(
    data: pd.DataFrame,
    device: Optional[t.device] = None,
):
    """
    Network computation based on the Lioness algorithm
    """
    num_samples = t.tensor(data.shape[0], dtype=t.float32)
    orig = t.from_numpy(data.to_numpy(dtype=np.float32, copy=False)).to(device)
    orig_transpose = t.transpose(orig, 0, 1)
    dot_prod = t.matmul(orig_transpose, orig)
    mean_vect = t.sum(orig, dim=0)
    std_vect = t.sum(t.pow(orig, 2), dim=0)
    glob_net = num_samples * t.corrcoef(orig_transpose)

    @t.jit.script
    def edge(num, mean_v, std_v, dot, glob, row):
        mean = mean_v - row
        d_q = t.sqrt((num - 1) * (std_v - t.pow(row, 2)) - t.pow(mean, 2))
        nom = (num - 1) * (dot - (t.reshape(row, (row.shape[0], 1)) * row)) - (
            t.reshape(mean, (row.shape[0], 1)) * mean
        )
        return t.flatten(
            glob - ((num - 1) * (nom / (t.reshape(d_q, (d_q.shape[0], 1)) * d_q)))
        )

    for i in range(data.shape[0]):
        yield edge(num_samples, mean_vect, std_vect, dot_prod, glob_net, orig[i])
