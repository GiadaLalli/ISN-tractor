import pandas as pd
import numpy as np
from numpy.random import randint, uniform

import pyperf


def discrete(n_individuals: int, m_snps: int) -> pd.DataFrame:
    return pd.DataFrame(
        randint(0, 3, size=(n_individuals, m_snps)),
        index=["sample_" + str(i) for i in range(n_individuals)],
        columns=["unmapped_feature_" + str(i) for i in range(m_snps)],
    )


def continuous(n_individuals: int, m_genes: int) -> pd.DataFrame:
    return pd.DataFrame(
        uniform(-100, 100, size=(n_individuals, m_genes)),
        index=["sample_" + str(i) for i in range(n_individuals)],
        columns=["mapped_feature_" + str(i) for i in range(m_genes)],
    )


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
