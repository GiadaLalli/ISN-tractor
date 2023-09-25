"""
This example shows the step-by-step workflow to make use of this library.
It also includes generation of all input data in the recommended format.
"""

import pandas as pd
import numpy as np

import isn_tractor.ibisn as it


def mock_mapped(size: tuple[int, int]) -> pd.DataFrame:
    "These data are generally gene expression-like data which are continuous."
    rows, cols = size
    data = np.random.uniform(0, 100, size=size)
    col_names = [f"mapped_feature_{i}" for i in range(cols)]
    index_names = [f"sample_{i}" for i in range(rows)]
    return pd.DataFrame(data, index=index_names, columns=col_names)


def mock_unmapped(size: tuple[int, int]) -> pd.DataFrame:
    "Unmapped data is always discrete (e.g. SNP data)."
    rows, cols = size
    data = np.random.randint(0, 3, size=size)
    col_names = [f"unmapped_feature_{i}" for i in range(cols)]
    index_names = [f"sample_{i}" for i in range(rows)]
    return pd.DataFrame(data, index=index_names, columns=col_names)


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
    n_chromosomes = 23

    # Compute number of rows
    n_rows = len(df.columns)

    # Generate random values for each column
    chrs = np.repeat(np.arange(1, n_chromosomes + 1), n_rows // n_chromosomes + 1)[
        :n_rows
    ]
    starts = np.arange(1, n_rows * 10 + 1, 10)
    stops = starts + 9

    # Assign values to rows based on input df
    df_rows = []
    for i, row_name in enumerate(df.columns):
        df_rows.append([chrs[i], starts[i], stops[i]])

    # Create dataframe
    data_frame = pd.DataFrame(df_rows, columns=column_names, index=df.columns)

    return data_frame


def unmapped_info(df):
    rows = df.shape[1]
    location = [2 * i for i in range(rows)]
    chromosome = sorted([(i % 23) + 1 for i in range(rows)])
    return pd.DataFrame(
        {"chr": chromosome[:rows], "location": location}, index=df.columns
    )


if __name__ == "__main__":
    u_df = mock_unmapped((200, 1_000_000))
    m_df = mock_mapped((200, 100))
    interact = interactions(100)
    mapped_info = mapped_info(m_df)
    unmapped_info = unmapped_info(u_df)

    # interaction mapping
    interact_unmapped, interact_mapped = it.map_interaction(
        interact, mapped_info=mapped_info, unmapped_info=unmapped_info, neighborhood=20
    )

    # ISNs computation
    # dense with continuous values
    d_isn = it.dense_isn(m_df)
    # sparse with:
    # discrete values
    s_c_isn = it.sparse_isn(
        u_df, interact_unmapped, interact_mapped, metric="pearson", pool="avg"
    )
    # continuous values
    s_d_isn = it.sparse_isn(
        m_df, interact_unmapped=None, interact_mapped=interact_mapped, metric="pearson"
    )
