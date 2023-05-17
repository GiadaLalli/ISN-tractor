import pytest

from pandas import DataFrame
from numpy.random import uniform

from isn_tractor.ibisn import dense_isn


def continuous(n_individuals: int, m_genes: int) -> DataFrame:
    return DataFrame(
        uniform(-100, 100, size=(n_individuals, m_genes)),
        index=["sample_" + str(i) for i in range(n_individuals)],
        columns=["mapped_feature_" + str(i) for i in range(m_genes)],
    )


def compute_dense_isn(data):
    for isn in dense_isn(data):
        del isn


@pytest.mark.benchmark
def test_dense_isn(benchmark):
    data = continuous(200, 1000)
    benchmark.pedantic(compute_dense_isn, args=(data,), rounds=20, iterations=3)
