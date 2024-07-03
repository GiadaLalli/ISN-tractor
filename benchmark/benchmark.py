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

    runner.timeit(
        "dense_500_1000",
        stmt="for isn in dense_isn(df): del isn",
        setup="from benchmark import continuous; from isn_tractor.ibisn import dense_isn; df = continuous(500, 1000)",
    )

    runner.timeit(
        "dense_500_2000",
        stmt="for isn in dense_isn(df): del isn",
        setup="from benchmark import continuous; from isn_tractor.ibisn import dense_isn; df = continuous(500, 2000)",
    )

    runner.timeit(
        "dense_500_3000",
        stmt="for isn in dense_isn(df): del isn",
        setup="from benchmark import continuous; from isn_tractor.ibisn import dense_isn; df = continuous(500, 3000)",
    )

    runner.timeit(
        "dense_1000_3000",
        stmt="for isn in dense_isn(df): del isn",
        setup="from benchmark import continuous; from isn_tractor.ibisn import dense_isn; df = continuous(1000, 3000)",
    )

    runner.timeit(
        "dense_2000_3000",
        stmt="for isn in dense_isn(df): del isn",
        setup="from benchmark import continuous; from isn_tractor.ibisn import dense_isn; df = continuous(2000, 3000)",
    )

    runner.timeit(
        "dense_2000_5000",
        stmt="for isn in dense_isn(df): del isn",
        setup="from benchmark import continuous; from isn_tractor.ibisn import dense_isn; df = continuous(2000, 5000)",
    )

    runner.timeit(
        "dense_2000_10000",
        stmt="for isn in dense_isn(df): del isn",
        setup="from benchmark import continuous; from isn_tractor.ibisn import dense_isn; df = continuous(2000, 10_000)",
    )

    runner.timeit(
        "dense_5000_10000",
        stmt="for isn in dense_isn(df): del isn",
        setup="from benchmark import continuous; from isn_tractor.ibisn import dense_isn; df = continuous(5000, 10_000)",
    )
