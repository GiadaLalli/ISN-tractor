from pandas import DataFrame
from numpy.random import randint, uniform

import pyperf

from isn_tractor.ibisn import dense_isn


def discrete(n_individuals: int, m_snps: int) -> DataFrame:
    return DataFrame(
        randint(0, 3, size=(n_individuals, m_snps)),
        index=["sample_" + str(i) for i in range(n_individuals)],
        columns=["unmapped_feature_" + str(i) for i in range(m_snps)],
    )


def continuous(n_individuals: int, m_genes: int) -> DataFrame:
    return DataFrame(
        uniform(-100, 100, size=(n_individuals, m_genes)),
        index=["sample_" + str(i) for i in range(n_individuals)],
        columns=["mapped_feature_" + str(i) for i in range(m_genes)],
    )


if __name__ == "__main__":
    runner = pyperf.Runner()

    bench = runner.timeit(
        "dense",
        stmt="dense_isn(df)",
        setup="from benchmark import continuous; from isn_tractor.ibisn import dense_isn; df = continuous(200, 1000)",
    )
