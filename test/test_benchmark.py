import pytest
import pandas as pd
import torch as t
import numpy as np

from isn_tractor.ibisn import dense_isn, sparse_isn

from benchmark.benchmark import continuous, interactions
from benchmark.dense_isn_offline import dense_isn_offline


def mapped_info(df):
    # Define column names
    column_names = ["chr", "start", "stop"]

    # Define number of chromosomes
    # n_chromosomes = 23
    n_chromosomes = 1
    # Compute number of rows
    n_rows = len(df.columns)

    # Generate random values for each column
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


def compute_dense_isn(data, device=None):
    for isn in dense_isn(data, device=device):
        del isn


def compute_dense_isn_offline(data, device=None):
    for isn in dense_isn_offline(data):
        del isn


@pytest.mark.benchmark_cpu_dense
def test_dense_200_1000_cpu(benchmark):
    data = continuous(200, 1000)
    benchmark(compute_dense_isn, data)


@pytest.mark.benchmark_cpu_dense
def test_dense_200_2000_cpu(benchmark):
    data = continuous(200, 2000)
    benchmark(compute_dense_isn, data)


@pytest.mark.benchmark_cpu_dense
def test_dense_200_3000_cpu(benchmark):
    data = continuous(200, 3000)
    benchmark(compute_dense_isn, data)


@pytest.mark.benchmark_cpu_dense
def test_dense_500_1000_cpu(benchmark):
    data = continuous(500, 1000)
    benchmark(compute_dense_isn, data)


@pytest.mark.benchmark_cpu_dense
def test_dense_500_2000_cpu(benchmark):
    data = continuous(500, 2000)
    benchmark(compute_dense_isn, data)


@pytest.mark.benchmark_cpu_dense
def test_dense_500_3000_cpu(benchmark):
    data = continuous(500, 3000)
    benchmark(compute_dense_isn, data)


@pytest.mark.benchmark_cpu_dense
def test_dense_1000_1000_cpu(benchmark):
    data = continuous(1000, 1000)
    benchmark(compute_dense_isn, data)


@pytest.mark.benchmark_cpu_dense
def test_dense_1000_2000_cpu(benchmark):
    data = continuous(1000, 2000)
    benchmark(compute_dense_isn, data)


@pytest.mark.benchmark_cpu_dense
def test_dense_1000_3000_cpu(benchmark):
    data = continuous(1000, 3000)
    benchmark(compute_dense_isn, data)


@pytest.mark.benchmark_cpu_dense
def test_dense_2000_1000_cpu(benchmark):
    data = continuous(2000, 1000)
    benchmark(compute_dense_isn, data)


@pytest.mark.benchmark_cpu_dense
def test_dense_2000_2000_cpu(benchmark):
    data = continuous(2000, 2000)
    benchmark(compute_dense_isn, data)


@pytest.mark.benchmark_cpu_dense
def test_dense_2000_3000_cpu(benchmark):
    data = continuous(2000, 3000)
    benchmark(compute_dense_isn, data)


@pytest.mark.benchmark_cpu_dense
def test_dense_2000_5000_cpu(benchmark):
    data = continuous(2000, 5000)
    benchmark(compute_dense_isn, data)


@pytest.mark.benchmark_cpu_dense
def test_dense_2000_10000_cpu(benchmark):
    data = continuous(2000, 10000)
    benchmark(compute_dense_isn, data)


@pytest.mark.benchmark_cpu_dense
def test_dense_offline_200_1000_cpu(benchmark):
    data = continuous(200, 1000)
    benchmark(compute_dense_isn_offline, data)


@pytest.mark.benchmark_cpu_dense
def test_dense_offline_200_2000_cpu(benchmark):
    data = continuous(200, 2000)
    benchmark(compute_dense_isn_offline, data)


@pytest.mark.benchmark_cpu_dense
def test_dense_offline_200_3000_cpu(benchmark):
    data = continuous(200, 3000)
    benchmark(compute_dense_isn_offline, data)


@pytest.mark.benchmark_cpu_dense
def test_dense_offline_500_1000_cpu(benchmark):
    data = continuous(500, 1000)
    benchmark(compute_dense_isn_offline, data)


@pytest.mark.benchmark_cpu_dense
def test_dense_offline_500_2000_cpu(benchmark):
    data = continuous(500, 2000)
    benchmark(compute_dense_isn_offline, data)


@pytest.mark.benchmark_cpu_dense
def test_dense_offline_500_3000_cpu(benchmark):
    data = continuous(500, 3000)
    benchmark(compute_dense_isn_offline, data)


@pytest.mark.benchmark_cpu_dense
def test_dense_offline_1000_1000_cpu(benchmark):
    data = continuous(1000, 1000)
    benchmark(compute_dense_isn_offline, data)


@pytest.mark.benchmark_cpu_dense
def test_dense_offline_1000_2000_cpu(benchmark):
    data = continuous(1000, 2000)
    benchmark(compute_dense_isn_offline, data)


@pytest.mark.benchmark_cpu_dense
def test_dense_offline_1000_3000_cpu(benchmark):
    data = continuous(1000, 3000)
    benchmark(compute_dense_isn_offline, data)


@pytest.mark.benchmark_cpu_dense
def test_dense_offline_2000_1000_cpu(benchmark):
    data = continuous(2000, 1000)
    benchmark(compute_dense_isn_offline, data)


@pytest.mark.benchmark_cpu_dense
def test_dense_offline_2000_2000_cpu(benchmark):
    data = continuous(2000, 2000)
    benchmark(compute_dense_isn_offline, data)


@pytest.mark.benchmark_cpu_dense
def test_dense_offline_2000_3000_cpu(benchmark):
    data = continuous(2000, 3000)
    benchmark(compute_dense_isn_offline, data)


@pytest.mark.benchmark_cpu_dense
def test_dense_offline_2000_5000_cpu(benchmark):
    data = continuous(2000, 5000)
    benchmark(compute_dense_isn_offline, data)


@pytest.mark.benchmark_cpu_dense
def test_dense_offline_2000_10000_cpu(benchmark):
    data = continuous(2000, 10000)
    benchmark(compute_dense_isn_offline, data)


@pytest.mark.benchmark_cuda
def test_dense_200_1000_cuda(benchmark):
    data = continuous(200, 1000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data, device), rounds=20, iterations=3)


@pytest.mark.benchmark_cuda
def test_dense_200_2000_cuda(benchmark):
    data = continuous(200, 2000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data, device), rounds=20, iterations=3)


@pytest.mark.benchmark_cuda
def test_dense_200_3000_cuda(benchmark):
    data = continuous(200, 3000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data, device), rounds=20, iterations=3)


@pytest.mark.benchmark_cuda
def test_dense_500_1000_cuda(benchmark):
    data = continuous(500, 1000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data, device), rounds=20, iterations=3)


@pytest.mark.benchmark_cuda
def test_dense_500_2000_cuda(benchmark):
    data = continuous(500, 2000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data, device), rounds=20, iterations=3)


@pytest.mark.benchmark_cuda
def test_dense_500_3000_cuda(benchmark):
    data = continuous(500, 3000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data, device), rounds=20, iterations=3)


@pytest.mark.benchmark_cuda
def test_dense_1000_1000_cuda(benchmark):
    data = continuous(1000, 1000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data, device), rounds=20, iterations=3)


@pytest.mark.benchmark_cuda
def test_dense_1000_2000_cuda(benchmark):
    data = continuous(1000, 2000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data, device), rounds=20, iterations=3)


@pytest.mark.benchmark_cuda
def test_dense_1000_3000_cuda(benchmark):
    data = continuous(1000, 3000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data, device), rounds=20, iterations=3)


@pytest.mark.benchmark_cuda
def test_dense_2000_1000_cuda(benchmark):
    data = continuous(2000, 1000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data, device), rounds=20, iterations=3)


@pytest.mark.benchmark_cuda
def test_dense_2000_2000_cuda(benchmark):
    data = continuous(2000, 2000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data, device), rounds=20, iterations=3)


@pytest.mark.benchmark_cuda
def test_dense_2000_3000_cuda(benchmark):
    data = continuous(2000, 3000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data, device), rounds=20, iterations=3)


@pytest.mark.benchmark_cuda
def test_dense_2000_5000_cuda(benchmark):
    data = continuous(2000, 5000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data, device), rounds=20, iterations=3)


@pytest.mark.benchmark_cuda
def test_dense_2000_10000_cuda(benchmark):
    data = continuous(2000, 10000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data, device), rounds=20, iterations=3)


def compute_sparse_isn(
    data,
    interact_unmapped,
    interact_mapped,
    metric,
    pool=None,
    device=None,
):
    for isn in sparse_isn(
        data,
        interact_unmapped=interact_unmapped,
        interact_mapped=interact_mapped,
        metric=metric,
        pool=pool,
        device=device,
    ):
        del isn


@pytest.fixture(scope="session")
def performance_test_data():
    return (continuous(18, 20), interactions(18))


@pytest.mark.performance_regression_test
def test_regression_biweight_max(benchmark, performance_test_data):
    data, interact = performance_test_data
    benchmark.pedantic(
        compute_sparse_isn,
        args=(data, None, interact, "biweight", "max"),
        rounds=20,
        iterations=5,
    )


@pytest.mark.performance_regression_test
def test_regression_biweight_avg(benchmark, performance_test_data):
    data, interact = performance_test_data
    benchmark.pedantic(
        compute_sparse_isn,
        args=(data, None, interact, "biweight", "avg"),
        rounds=20,
        iterations=5,
    )


@pytest.mark.performance_regression_test
def test_regression_biweight_none(benchmark, performance_test_data):
    data, interact = performance_test_data
    benchmark.pedantic(
        compute_sparse_isn,
        args=(data, None, interact, "biweight"),
        rounds=20,
        iterations=5,
    )


@pytest.mark.performance_regression_test
def test_regression_pearson_max(benchmark, performance_test_data):
    data, interact = performance_test_data
    benchmark.pedantic(
        compute_sparse_isn,
        args=(data, None, interact, "pearson", "max"),
        rounds=20,
        iterations=5,
    )


@pytest.mark.performance_regression_test
def test_regression_pearson_avg(benchmark, performance_test_data):
    data, interact = performance_test_data
    benchmark.pedantic(
        compute_sparse_isn,
        args=(data, None, interact, "pearson", "avg"),
        rounds=20,
        iterations=5,
    )


@pytest.mark.performance_regression_test
def test_regression_pearson_none(benchmark, performance_test_data):
    data, interact = performance_test_data
    benchmark.pedantic(
        compute_sparse_isn,
        args=(data, None, interact, "pearson"),
        rounds=20,
        iterations=5,
    )


@pytest.mark.performance_regression_test
def test_regression_spearman_max(benchmark, performance_test_data):
    data, interact = performance_test_data
    benchmark.pedantic(
        compute_sparse_isn,
        args=(data, None, interact, "spearman", "max"),
        rounds=20,
        iterations=5,
    )


@pytest.mark.performance_regression_test
def test_regression_spearman_avg(benchmark, performance_test_data):
    data, interact = performance_test_data
    benchmark.pedantic(
        compute_sparse_isn,
        args=(data, None, interact, "spearman", "avg"),
        rounds=20,
        iterations=5,
    )


@pytest.mark.performance_regression_test
def test_regression_spearman_none(benchmark, performance_test_data):
    data, interact = performance_test_data
    benchmark.pedantic(
        compute_sparse_isn,
        args=(data, None, interact, "spearman"),
        rounds=20,
        iterations=5,
    )


@pytest.mark.performance_regression_test
def test_regression_dot_max(benchmark, performance_test_data):
    data, interact = performance_test_data
    benchmark.pedantic(
        compute_sparse_isn,
        args=(data, None, interact, "dot", "max"),
        rounds=20,
        iterations=5,
    )


@pytest.mark.performance_regression_test
def test_regression_dot_avg(benchmark, performance_test_data):
    data, interact = performance_test_data
    benchmark.pedantic(
        compute_sparse_isn,
        args=(data, None, interact, "dot", "avg"),
        rounds=20,
        iterations=5,
    )


@pytest.mark.performance_regression_test
def test_regression_dot_none(benchmark, performance_test_data):
    data, interact = performance_test_data
    benchmark.pedantic(
        compute_sparse_isn,
        args=(data, None, interact, "dot"),
        rounds=20,
        iterations=5,
    )


@pytest.mark.performance_regression_test
def test_regression_dense(benchmark, performance_test_data):
    data, _ = performance_test_data
    benchmark.pedantic(
        compute_dense_isn,
        args=(data,),
        rounds=20,
        iterations=5,
    )


@pytest.mark.benchmark_cpu_sparse
def test_sparse_200_500_biweight_midcorrelation_cpu(benchmark):
    data = continuous(200, 500)
    interact = interactions(500)
    benchmark(compute_sparse_isn, data, None, interact, "biweight")


@pytest.mark.benchmark_cpu_sparse
def test_sparse_200_1000_biweight_midcorrelation_cpu(benchmark):
    data = continuous(200, 1000)
    interact = interactions(1000)
    benchmark(compute_sparse_isn, data, None, interact, "biweight")


@pytest.mark.benchmark_cpu_sparse
def test_sparse_500_500_biweight_midcorrelation_cpu(benchmark):
    data = continuous(500, 500)
    interact = interactions(500)
    benchmark(compute_sparse_isn, data, None, interact, "biweight")


@pytest.mark.benchmark_cpu_sparse
def test_sparse_500_1000_biweight_midcorrelation_cpu(benchmark):
    data = continuous(500, 1000)
    interact = interactions(1000)
    benchmark(compute_sparse_isn, data, None, interact, "biweight")


@pytest.mark.benchmark_cpu_sparse
def test_sparse_200_500_pearson_cpu(benchmark):
    data = continuous(200, 500)
    interact = interactions(500)
    benchmark(compute_sparse_isn, data, None, interact, "pearson")


@pytest.mark.benchmark_cpu_sparse
def test_sparse_200_1000_pearson_cpu(benchmark):
    data = continuous(200, 1000)
    interact = interactions(1000)
    benchmark(compute_sparse_isn, data, None, interact, "pearson")


@pytest.mark.benchmark_cpu_sparse
def test_sparse_500_500_pearson_cpu(benchmark):
    data = continuous(500, 500)
    interact = interactions(500)
    benchmark(compute_sparse_isn, data, None, interact, "pearson")


@pytest.mark.benchmark_cpu_sparse
def test_sparse_500_1000_pearson_cpu(benchmark):
    data = continuous(500, 1000)
    interact = interactions(1000)
    benchmark(compute_sparse_isn, data, None, interact, "pearson")


@pytest.mark.benchmark_cuda
def test_sparse_200_10000_pearson_cuda(benchmark):
    data = continuous(200, 10000)
    i_m = interactions(10000)
    device = t.device("cuda")
    benchmark.pedantic(
        compute_sparse_isn,
        args=(data, None, i_m, "pearson", None, device),
        rounds=20,
        iterations=3,
    )


@pytest.mark.benchmark_cuda
def test_sparse_500_10000_pearson_cuda(benchmark):
    data = continuous(500, 10000)
    i_m = interactions(10000)
    device = t.device("cuda")
    benchmark.pedantic(
        compute_sparse_isn,
        args=(data, None, i_m, "pearson", None, device),
        rounds=20,
        iterations=3,
    )


@pytest.mark.benchmark_cuda
def test_sparse_1000_10000_pearson_cuda(benchmark):
    data = continuous(1000, 10000)
    i_m = interactions(7000)
    device = t.device("cuda")
    benchmark.pedantic(
        compute_sparse_isn,
        args=(data, None, i_m, "pearson", None, device),
        rounds=20,
        iterations=3,
    )


@pytest.mark.benchmark_cuda
def test_sparse_2000_10000_pearson_cuda(benchmark):
    data = continuous(2000, 10000)
    i_m = interactions(8000)
    device = t.device("cuda")
    benchmark.pedantic(
        compute_sparse_isn,
        args=(data, None, i_m, "pearson", None, device),
        rounds=20,
        iterations=3,
    )


@pytest.mark.benchmark_cuda
def test_dense_200_10000_cuda(benchmark):
    data = continuous(200, 10000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data, device), rounds=20, iterations=3)


@pytest.mark.benchmark_cuda
def test_dense_500_5000_cuda(benchmark):
    data = continuous(500, 5000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data, device), rounds=20, iterations=3)


@pytest.mark.benchmark_cuda
def test_dense_500_10000_cuda(benchmark):
    data = continuous(500, 10000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data, device), rounds=20, iterations=3)


@pytest.mark.benchmark_cuda
def test_dense_1000_5000_cuda(benchmark):
    data = continuous(1000, 5000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data, device), rounds=20, iterations=3)


@pytest.mark.benchmark_cuda
def test_dense_1000_10000_cuda(benchmark):
    data = continuous(1000, 10000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data, device), rounds=20, iterations=3)


###########
@pytest.mark.benchmark_cuda
def test_dense_offline_200_1000_cuda(benchmark):
    data = continuous(200, 1000)
    device = t.device("cuda")
    benchmark.pedantic(
        compute_dense_isn_offline, args=(data, device), rounds=20, iterations=3
    )


@pytest.mark.benchmark_cuda
def test_dense_offline_200_2000_cuda(benchmark):
    data = continuous(200, 2000)
    device = t.device("cuda")
    benchmark.pedantic(
        compute_dense_isn_offline, args=(data, device), rounds=20, iterations=3
    )


@pytest.mark.benchmark_cuda
def test_dense_offline_200_3000_cuda(benchmark):
    data = continuous(200, 3000)
    device = t.device("cuda")
    benchmark.pedantic(
        compute_dense_isn_offline, args=(data, device), rounds=20, iterations=3
    )


@pytest.mark.benchmark_cuda
def test_dense_offline_500_1000_cuda(benchmark):
    data = continuous(500, 1000)
    device = t.device("cuda")
    benchmark.pedantic(
        compute_dense_isn_offline, args=(data, device), rounds=20, iterations=3
    )


@pytest.mark.benchmark_cuda
def test_dense_offline_500_2000_cuda(benchmark):
    data = continuous(500, 2000)
    device = t.device("cuda")
    benchmark.pedantic(
        compute_dense_isn_offline, args=(data, device), rounds=20, iterations=3
    )


@pytest.mark.benchmark_cuda
def test_dense_offline_500_3000_cuda(benchmark):
    data = continuous(500, 3000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data, device), rounds=20, iterations=3)


@pytest.mark.benchmark_cuda
def test_dense_offline_1000_1000_cuda(benchmark):
    data = continuous(1000, 1000)
    device = t.device("cuda")
    benchmark.pedantic(
        compute_dense_isn_offline, args=(data, device), rounds=20, iterations=3
    )


@pytest.mark.benchmark_cuda
def test_dense_offline_1000_2000_cuda(benchmark):
    data = continuous(1000, 2000)
    device = t.device("cuda")
    benchmark.pedantic(
        compute_dense_isn_offline, args=(data, device), rounds=20, iterations=3
    )


@pytest.mark.benchmark_cuda
def test_dense_offline_1000_3000_cuda(benchmark):
    data = continuous(1000, 3000)
    device = t.device("cuda")
    benchmark.pedantic(
        compute_dense_isn_offline, args=(data, device), rounds=20, iterations=3
    )


@pytest.mark.benchmark_cuda
def test_dense_offline_2000_1000_cuda(benchmark):
    data = continuous(2000, 1000)
    device = t.device("cuda")
    benchmark.pedantic(
        compute_dense_isn_offline, args=(data, device), rounds=20, iterations=3
    )


@pytest.mark.benchmark_cuda
def test_dense_offline_2000_2000_cuda(benchmark):
    data = continuous(2000, 2000)
    device = t.device("cuda")
    benchmark.pedantic(
        compute_dense_isn_offline, args=(data, device), rounds=20, iterations=3
    )


@pytest.mark.benchmark_cuda
def test_dense_offline_2000_3000_cuda(benchmark):
    data = continuous(2000, 3000)
    device = t.device("cuda")
    benchmark.pedantic(
        compute_dense_isn_offline, args=(data, device), rounds=20, iterations=3
    )


@pytest.mark.benchmark_cuda
def test_dense_offline_2000_5000_cuda(benchmark):
    data = continuous(2000, 5000)
    device = t.device("cuda")
    benchmark.pedantic(
        compute_dense_isn_offline, args=(data, device), rounds=20, iterations=3
    )


@pytest.mark.benchmark_cuda
def test_dense_offline_2000_10000_cuda(benchmark):
    data = continuous(2000, 10000)
    device = t.device("cuda")
    benchmark.pedantic(
        compute_dense_isn_offline, args=(data, device), rounds=20, iterations=3
    )
