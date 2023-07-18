import pytest
import pandas as pd
import torch as t
import numpy as np
from pandas import DataFrame
from numpy.random import uniform, randint

from isn_tractor.ibisn import dense_isn, sparse_isn

"""
def discrete(n_individuals: int, m_genes: int) -> DataFrame:
    return DataFrame(
        np.random.randint(0, 3, size=(n_individuals, m_genes)),
        index=["sample_" + str(i) for i in range(n_individuals)],
        columns=["unmapped_feature_" + str(i) for i in range(m_genes)],
    )"""


def interactions(n_rows):
    features = [f"mapped_feature_{i}" for i in range(n_rows)]
    interact = []
    for i in range(len(features)):
        other_features = features[:i] + features[i + 1 :]
        n_interact = np.random.randint(1, n_rows)
        interact_features = np.random.choice(
            other_features, size=n_interact, replace=False
        )
        for j in range(n_interact):
            interact.append((features[i], interact_features[j]))
    interact_df = pd.DataFrame(interact, columns=["feature_1", "feature_2"])

    # Remove 30% of random rows
    interact_df = interact_df.sample(frac=0.7, random_state=42)

    # Sort by index
    interact_df = interact_df.sort_index()

    return interact_df


def mapped_info(df):
    # Define column names
    column_names = ["chr", "start", "stop"]

    # Define number of chromosomes
    # n_chromosomes = 23
    n_chromosomes = 1
    # Compute number of rows
    n_rows = len(df.columns)

    # Generate random values for each column
    chrs = np.repeat(np.arange(1, n_chromosomes + 1), n_rows // n_chromosomes + 1)[
        :n_rows
    ]
    starts = np.arange(1, n_rows * 10000 + 1, 10000)
    stops = starts + 9

    # Assign values to rows based on input df
    df_rows = []
    for i, row_name in enumerate(df.columns):
        # df_rows.append([chrs[i], starts[i], stops[i]])
        df_rows.append([n_chromosomes, starts[i], stops[i]])

    # Create dataframe
    data_frame = pd.DataFrame(df_rows, columns=column_names, index=df.columns)

    return data_frame


def unmapped_info(df):
    rows = df.shape[1]
    location = [2 * i for i in range(rows)]
    # chromosome = sorted([(i % 23) + 1 for i in range(rows)])
    chromosome = 1
    return pd.DataFrame({"chr": chromosome, "location": location}, index=df.columns)


def continuous(n_individuals: int, m_genes: int) -> DataFrame:
    return DataFrame(
        uniform(-100, 100, size=(n_individuals, m_genes)),
        index=["sample_" + str(i) for i in range(n_individuals)],
        columns=["mapped_feature_" + str(i) for i in range(m_genes)],
    )


def compute_dense_isn(data, device=None):
    for isn in dense_isn(data, device=device):
        del isn


@pytest.mark.benchmark
def test_dense_200_500_cpu(benchmark):
    data = continuous(200, 500)
    benchmark(compute_dense_isn, data)


@pytest.mark.benchmark
def test_dense_200_1000_cuda(benchmark):
    data = continuous(200, 1000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data, device), rounds=20, iterations=3)


@pytest.mark.benchmark
def test_dense_200_2000_cuda(benchmark):
    data = continuous(200, 2000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data, device), rounds=20, iterations=3)


@pytest.mark.benchmark
def test_dense_200_3000_cuda(benchmark):
    data = continuous(200, 3000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data, device), rounds=20, iterations=3)


@pytest.mark.benchmark
def test_dense_500_1000_cuda(benchmark):
    data = continuous(500, 1000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data, device), rounds=20, iterations=3)


@pytest.mark.benchmark
def test_dense_500_2000_cuda(benchmark):
    data = continuous(500, 2000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data, device), rounds=20, iterations=3)


@pytest.mark.benchmark
def test_dense_500_3000_cuda(benchmark):
    data = continuous(500, 3000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data, device), rounds=20, iterations=3)


@pytest.mark.benchmark
def test_dense_1000_1000_cuda(benchmark):
    data = continuous(1000, 1000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data, device), rounds=20, iterations=3)


@pytest.mark.benchmark
def test_dense_1000_2000_cuda(benchmark):
    data = continuous(1000, 2000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data, device), rounds=20, iterations=3)


@pytest.mark.benchmark
def test_dense_1000_3000_cuda(benchmark):
    data = continuous(1000, 3000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data, device), rounds=20, iterations=3)


@pytest.mark.benchmark
def test_dense_2000_1000_cuda(benchmark):
    data = continuous(2000, 1000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data, device), rounds=20, iterations=3)


@pytest.mark.benchmark
def test_dense_2000_2000_cuda(benchmark):
    data = continuous(2000, 2000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data, device), rounds=20, iterations=3)


@pytest.mark.benchmark
def test_dense_2000_3000_cuda(benchmark):
    data = continuous(2000, 3000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data, device), rounds=20, iterations=3)


@pytest.mark.benchmark
def test_dense_2000_5000_cuda(benchmark):
    data = continuous(2000, 5000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data, device), rounds=20, iterations=3)


@pytest.mark.benchmark
def test_dense_2000_10000_cuda(benchmark):
    data = continuous(2000, 10000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data, device), rounds=20, iterations=3)


def compute_sparse_isn(
    data, interact_unmapped, interact_mapped, metric="incremental_pearson", pool=None
):
    for isn in sparse_isn(
        data,
        interact_unmapped=interact_unmapped,
        interact_mapped=interact_mapped,
        metric=metric,
        pool=pool,
    ):
        del isn


@pytest.mark.benchmark
def test_sparse_200_500_cpu(benchmark):
    data = continuous(200, 500)
    interact = interactions(500)
    benchmark(compute_sparse_isn, data, None, interact)


@pytest.mark.benchmark
def test_sparse_200_10000_cuda(benchmark):
    data = continuous(200, 10000)
    i_m = interactions(5000)
    # device = t.device("cuda")
    benchmark.pedantic(
        compute_sparse_isn,
        args=(data, None, i_m, "incremental_pearson", None),
        rounds=20,
        iterations=3,
    )


@pytest.mark.benchmark
def test_sparse_500_10000_cuda(benchmark):
    data = continuous(500, 10000)
    i_m = interactions(5200)
    # device = t.device("cuda")
    benchmark.pedantic(
        compute_sparse_isn,
        args=(data, None, i_m, "incremental_pearson", None),
        rounds=20,
        iterations=3,
    )


@pytest.mark.benchmark
def test_sparse_1000_10000_cuda(benchmark):
    data = continuous(1000, 10000)
    i_m = interactions(7000)
    # device = t.device("cuda")
    benchmark.pedantic(
        compute_sparse_isn,
        args=(data, None, i_m, "incremental_pearson", None),
        rounds=20,
        iterations=3,
    )


@pytest.mark.benchmark
def test_sparse_2000_10000_cuda(benchmark):
    data = continuous(2000, 10000)
    i_m = interactions(8000)
    # device = t.device("cuda")
    benchmark.pedantic(
        compute_sparse_isn,
        args=(data, None, i_m, "incremental_pearson", None),
        rounds=20,
        iterations=3,
    )


@pytest.mark.benchmark
def test_dense_200_10000_cuda(benchmark):
    data = continuous(200, 10000)
    # device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data,), rounds=20, iterations=3)


@pytest.mark.benchmark
def test_dense_500_5000_cuda(benchmark):
    data = continuous(500, 5000)
    # device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data,), rounds=20, iterations=3)


@pytest.mark.benchmark
def test_dense_500_10000_cuda(benchmark):
    data = continuous(500, 10000)
    # device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data,), rounds=20, iterations=3)


@pytest.mark.benchmark
def test_dense_1000_5000_cuda(benchmark):
    data = continuous(1000, 5000)
    # device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data,), rounds=20, iterations=3)


@pytest.mark.benchmark
def test_dense_1000_10000_cuda(benchmark):
    data = continuous(1000, 10000)
    # device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data,), rounds=20, iterations=3)
