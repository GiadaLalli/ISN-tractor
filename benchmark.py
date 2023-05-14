from pandas import DataFrame
from numpy.random import randint, uniform

import matplotlib.pyplot as plt
import scipy.stats as stats

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
    # df = continuous(10, 20)
    runner.timeit(
        "dense",
        stmt="dense_isn(df)",
        setup="from benchmark import continuous; from isn_tractor.ibisn import dense_isn; df = continuous(200, 1000)",
    )
    # runner.bench_func("dense", dense_isn, df, inner_loops=50)
    # print(bench.mean())
    # values = sorted(bench.get_values())
    # fit = stats.norm.pdf(values, bench.mean(), bench.stdev())
    # plt.plot(values, fit, "-o", label="mean-stdev")
    # plt.hist(values, bins=10)
    # plt.show()
