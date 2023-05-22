import pytest
import torch as t

from pandas import DataFrame
from numpy.random import uniform

from isn_tractor.ibisn import dense_isn


def continuous(n_individuals: int, m_genes: int) -> DataFrame:
    return DataFrame(
        uniform(-100, 100, size=(n_individuals, m_genes)),
        index=["sample_" + str(i) for i in range(n_individuals)],
        columns=["mapped_feature_" + str(i) for i in range(m_genes)],
    )


def compute_dense_isn(data, device):
    for isn in dense_isn(data, device=t.device("cuda")):
        del isn


@pytest.mark.benchmark
def test_dense_200_1000(benchmark):
    data = continuous(200, 1000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data,device), rounds=20, iterations=3)

@pytest.mark.benchmark
def test_dense_200_2000(benchmark):
    data = continuous(200, 2000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data,device), rounds=20, iterations=3)

@pytest.mark.benchmark
def test_dense_200_3000(benchmark):
    data = continuous(200, 3000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data,device), rounds=20, iterations=3)

@pytest.mark.benchmark
def test_dense_500_1000(benchmark):
    data = continuous(500, 1000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data,device), rounds=20, iterations=3)

@pytest.mark.benchmark
def test_dense_500_2000(benchmark):
    data = continuous(500, 2000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data,device), rounds=20, iterations=3)

@pytest.mark.benchmark
def test_dense_500_3000(benchmark):
    data = continuous(500, 3000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data,device), rounds=20, iterations=3)

@pytest.mark.benchmark
def test_dense_1000_1000(benchmark):
    data = continuous(1000, 1000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data,device), rounds=20, iterations=3)

@pytest.mark.benchmark
def test_dense_1000_2000(benchmark):
    data = continuous(1000, 2000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data,device), rounds=20, iterations=3)

@pytest.mark.benchmark
def test_dense_1000_3000(benchmark):
    data = continuous(1000, 3000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data,device), rounds=20, iterations=3)

@pytest.mark.benchmark
def test_dense_2000_1000(benchmark):
    data = continuous(2000, 1000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data,device), rounds=20, iterations=3)

@pytest.mark.benchmark
def test_dense_2000_2000(benchmark):
    data = continuous(2000, 2000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data,device), rounds=20, iterations=3)

@pytest.mark.benchmark
def test_dense_2000_3000(benchmark):
    data = continuous(2000, 3000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data,device), rounds=20, iterations=3)

@pytest.mark.benchmark
def test_dense_2000_5000(benchmark):
    data = continuous(2000, 5000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data,device), rounds=20, iterations=3)

@pytest.mark.benchmark
def test_dense_2000_10000(benchmark):
    data = continuous(2000, 10000)
    device = t.device("cuda")
    benchmark.pedantic(compute_dense_isn, args=(data,device), rounds=20, iterations=3)
