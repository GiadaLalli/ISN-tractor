import pytest
from isn_tractor.ibisn import sparse_isn, dense_isn, __spearman_metric
from benchmark.dense_isn_offline import dense_isn_offline

# from numpy import array, concatenate, corrcoef, float32, nan, arange, repeat, tile
import numpy as np
import pandas as pd
from pandas.testing import assert_frame_equal
from sklearn.metrics import normalized_mutual_info_score as mutual_info
import torch as t
from scipy.stats import pearsonr, spearmanr


def my_mutual_info_metric(first, second):
    if (first.dim(), second.dim()) == (1, 1):
        return mutual_info(first.numpy(), second.numpy())

    scores = t.zeros((first.shape[1], second.shape[1]))
    for i in range(first.shape[1]):
        for j in range(second.shape[1]):
            scores[i, j] = mutual_info(first[:, i], second[:, j])
    return scores


def my_pearson_metric(first, second):
    if (first.dim(), second.dim()) == (1, 1):
        return t.tensor(
            pearsonr(first.numpy(), second.numpy()).statistic, dtype=t.float32
        )

    combined = np.concatenate([first, second], axis=1)
    return t.tensor(
        np.corrcoef(combined.T)[: first.shape[1], first.shape[1]], dtype=t.float32
    )


def my_spearman_metric(first, second):
    return t.tensor(
        spearmanr(first.numpy(), second.numpy()).statistic[
            : first.shape[1], first.shape[1] :
        ]
    )


def mk_sparse_isn(data, unmapped, mapped, metric, pool=None) -> pd.DataFrame:
    return pd.DataFrame(
        np.column_stack(
            [edge for edge in sparse_isn(data, unmapped, mapped, metric, pool)]
        ),
        columns=[f"{a}_{b}" for (a, b) in mapped.values],
    )


def test_empty_inputs():
    snp_data = pd.DataFrame()
    interact_snp = []
    interact_gene = pd.DataFrame()
    with pytest.raises(ValueError):
        mk_sparse_isn(snp_data, interact_snp, interact_gene, "pearson", "avg"),


def test_snp_pearson_avg():
    snp_data = pd.DataFrame(
        [(1, 0), (1, 2), (2, 1), (0, 0), (1, 2)], columns=["snp_jcstj", "snp_dvxkv"]
    )
    interact_snp = [
        (
            np.array(["snp_jcstj", "snp_dvxkv"], dtype=object),
            np.array(["snp_jcstj", "snp_dvxkv"], dtype=object),
        )
    ]
    interact_gene = pd.DataFrame(
        [("gene_vcbc", "gene_pipx")], columns=["gene_id_1", "gene_id_2"]
    )
    assert_frame_equal(
        mk_sparse_isn(snp_data, interact_snp, interact_gene, "pearson", "avg"),
        pd.DataFrame(
            [
                (0.531081,),
                (0.531081,),
                (0.229183,),
                (1.732039,),
                (0.531081,),
            ],
            columns=["gene_vcbc_gene_pipx"],
            dtype=np.float32,
        ),
    )


def test_snp_pearson_max():
    snp_data = pd.DataFrame(
        [(1, 0), (1, 2), (2, 1), (0, 0), (1, 2)], columns=["snp_jcstj", "snp_dvxkv"]
    )
    interact_snp = [
        (
            np.array(["snp_jcstj", "snp_dvxkv"], dtype=object),
            np.array(["snp_jcstj", "snp_dvxkv"], dtype=object),
        )
    ]
    interact_gene = pd.DataFrame(
        [("gene_vcbc", "gene_pipx")], columns=["gene_id_1", "gene_id_2"]
    )
    assert_frame_equal(
        mk_sparse_isn(snp_data, interact_snp, interact_gene, "pearson", "max"),
        pd.DataFrame(
            [
                (1.0,),
                (1.0,),
                (1.0,),
                (1.0,),
                (1.0,),
            ],
            columns=["gene_vcbc_gene_pipx"],
            dtype=np.float32,
        ),
    )


def test_snp_spearman_avg():
    snp_data = pd.DataFrame(
        [(1, 0), (1, 2), (2, 1), (0, 0), (1, 2)], columns=["snp_jcstj", "snp_dvxkv"]
    )
    interact_snp = [
        (
            np.array(["snp_jcstj", "snp_dvxkv"], dtype=object),
            np.array(["snp_jcstj", "snp_dvxkv"], dtype=object),
        )
    ]
    interact_gene = pd.DataFrame(
        [("gene_vcbc", "gene_pipx")], columns=["gene_id_1", "gene_id_2"]
    )

    assert_frame_equal(
        mk_sparse_isn(snp_data, interact_snp, interact_gene, "spearman", "avg"),
        pd.DataFrame(
            [
                (0.845841,),
                (0.289546,),
                (0.106168,),
                (1.609025,),
                (0.289546,),
            ],
            columns=["gene_vcbc_gene_pipx"],
            dtype=np.float32,
        ),
    )


def test_snp_spearman_max():
    snp_data = pd.DataFrame(
        [(1, 0), (1, 2), (2, 1), (0, 0), (1, 2)], columns=["snp_jcstj", "snp_dvxkv"]
    )
    interact_snp = [
        (
            np.array(["snp_jcstj", "snp_dvxkv"], dtype=object),
            np.array(["snp_jcstj", "snp_dvxkv"], dtype=object),
        )
    ]
    interact_gene = pd.DataFrame(
        [("gene_vcbc", "gene_pipx")], columns=["gene_id_1", "gene_id_2"]
    )
    assert_frame_equal(
        mk_sparse_isn(snp_data, interact_snp, interact_gene, "spearman", "max"),
        pd.DataFrame(
            [
                (1.0,),
                (1.0,),
                (1.0,),
                (1.0,),
                (1.0,),
            ],
            columns=["gene_vcbc_gene_pipx"],
            dtype=np.float32,
        ),
    )


def test_snp_mutual_info_avg():
    snp_data = pd.DataFrame(
        [(1, 0), (1, 2), (2, 1), (0, 0), (1, 2)], columns=["snp_jcstj", "snp_dvxkv"]
    )
    interact_snp = [
        (
            np.array(["snp_jcstj", "snp_dvxkv"], dtype=object),
            np.array(["snp_jcstj", "snp_dvxkv"], dtype=object),
        )
    ]
    interact_gene = pd.DataFrame(
        [("gene_vcbc", "gene_pipx")], columns=["gene_id_1", "gene_id_2"]
    )
    assert_frame_equal(
        mk_sparse_isn(
            snp_data, interact_snp, interact_gene, my_mutual_info_metric, "avg"
        ),
        pd.DataFrame(
            [
                (0.178174,),
                (0.844840,),
                (1.490751,),
                (0.77414,),
                (0.844840,),
            ],
            columns=["gene_vcbc_gene_pipx"],
            dtype=np.float32,
        ),
    )


def test_snp_mutual_info_max():
    snp_data = pd.DataFrame(
        [(1, 0), (1, 2), (2, 1), (0, 0), (1, 2)], columns=["snp_jcstj", "snp_dvxkv"]
    )
    interact_snp = [
        (
            np.array(["snp_jcstj", "snp_dvxkv"], dtype=object),
            np.array(["snp_jcstj", "snp_dvxkv"], dtype=object),
        )
    ]
    interact_gene = pd.DataFrame(
        [("gene_vcbc", "gene_pipx")], columns=["gene_id_1", "gene_id_2"]
    )
    assert_frame_equal(
        mk_sparse_isn(
            snp_data, interact_snp, interact_gene, my_mutual_info_metric, "max"
        ),
        pd.DataFrame(
            [
                (1.0,),
                (1.0,),
                (1.0,),
                (1.0,),
                (1.0,),
            ],
            columns=["gene_vcbc_gene_pipx"],
            dtype=np.float32,
        ),
    )


def test_snp_dot_avg():
    snp_data = pd.DataFrame(
        [(1, 0), (1, 2), (2, 1), (0, 0), (1, 2)], columns=["snp_jcstj", "snp_dvxkv"]
    )
    interact_snp = [
        (
            np.array(["snp_jcstj", "snp_dvxkv"], dtype=object),
            np.array(["snp_jcstj", "snp_dvxkv"], dtype=object),
        )
    ]
    interact_gene = pd.DataFrame(
        [("gene_vcbc", "gene_pipx")], columns=["gene_id_1", "gene_id_2"]
    )
    assert_frame_equal(
        mk_sparse_isn(snp_data, interact_snp, interact_gene, "dot", "avg"),
        pd.DataFrame(
            [
                (8.0,),
                (16.0,),
                (16.0,),
                (7.0,),
                (16.0,),
            ],
            columns=["gene_vcbc_gene_pipx"],
            dtype=np.float32,
        ),
    )


def test_snp_dot_max():
    snp_data = pd.DataFrame(
        [(1, 0), (1, 2), (2, 1), (0, 0), (1, 2)], columns=["snp_jcstj", "snp_dvxkv"]
    )
    interact_snp = [
        (
            np.array(["snp_jcstj", "snp_dvxkv"], dtype=object),
            np.array(["snp_jcstj", "snp_dvxkv"], dtype=object),
        )
    ]
    interact_gene = pd.DataFrame(
        [("gene_vcbc", "gene_pipx")], columns=["gene_id_1", "gene_id_2"]
    )
    assert_frame_equal(
        mk_sparse_isn(snp_data, interact_snp, interact_gene, "dot", "max"),
        pd.DataFrame(
            [
                (9.0,),
                (21.0,),
                (13.0,),
                (9.0,),
                (21.0,),
            ],
            columns=["gene_vcbc_gene_pipx"],
            dtype=np.float32,
        ),
    )


def test_snp_larger():
    snp_data = pd.DataFrame(
        [(1, 0, 1, 1), (1, 2, 2, 0), (2, 1, 0, 2), (0, 0, 1, 0), (1, 2, 0, 0)],
        columns=["snp_a", "snp_b", "snp_c", "snp_d"],
    )
    interact_snp = [
        (
            np.array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
            np.array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
        ),
        (
            np.array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
            np.array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
        ),
        (
            np.array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
            np.array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
        ),
        (
            np.array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
            np.array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
        ),
    ]
    interact_gene = pd.DataFrame(
        [
            ("gene_a", "gene_b"),
            ("gene_a", "gene_c"),
            ("gene_b", "gene_c"),
            ("gene_c", "gene_d"),
        ],
        columns=["gene_id_1", "gene_id_2"],
    )

    computed = mk_sparse_isn(
        snp_data, interact_snp, interact_gene, "pearson", "average"
    )
    computed_old = mk_sparse_isn(
        snp_data, interact_snp, interact_gene, my_pearson_metric, "average"
    )

    assert_frame_equal(computed, computed_old)

    assert_frame_equal(
        computed,
        pd.DataFrame(
            [
                (0.3354356, 0.3354356, 0.3354356, 0.3354356),
                (0.5798347, 0.5798347, 0.5798347, 0.5798347),
                (0.2412484, 0.2412484, 0.2412484, 0.2412484),
                (0.9778545, 0.9778545, 0.9778545, 0.9778545),
                (0.3727278, 0.3727278, 0.3727278, 0.3727278),
            ],
            columns=[
                "gene_a_gene_b",
                "gene_a_gene_c",
                "gene_b_gene_c",
                "gene_c_gene_d",
            ],
            dtype=np.float32,
        ),
    )


def test_invalid_metric_without_data():
    snp_data = pd.DataFrame()
    interact_snp = []
    interact_gene = pd.DataFrame()

    with pytest.raises(ValueError):
        mk_sparse_isn(snp_data, interact_snp, interact_gene, "metric", "avg")


def test_invalid_metric_with_data():
    snp_data = pd.DataFrame(
        [(1, 0), (1, 2), (2, 1), (0, 0), (1, 2)], columns=["snp_jcstj", "snp_dvxkv"]
    )
    interact_snp = [
        (
            np.array(["snp_jcstj", "snp_dvxkv"], dtype=object),
            np.array(["snp_jcstj", "snp_dvxkv"], dtype=object),
        )
    ]
    interact_gene = pd.DataFrame(
        [("gene_vcbc", "gene_pipx")], columns=["gene_id_1", "gene_id_2"]
    )

    with pytest.raises(ValueError):
        mk_sparse_isn(snp_data, interact_snp, interact_gene, "metric", "avg")


def test_invalid_pool_without_data():
    snp_data = pd.DataFrame()
    interact_snp = []
    interact_gene = pd.DataFrame()

    with pytest.raises(ValueError):
        mk_sparse_isn(snp_data, interact_snp, interact_gene, "pearson", "pool")


def test_invalid_pool_with_data():
    snp_data = pd.DataFrame(
        [(1, 0), (1, 2), (2, 1), (0, 0), (1, 2)], columns=["snp_jcstj", "snp_dvxkv"]
    )
    interact_snp = [
        (
            np.array(["snp_jcstj", "snp_dvxkv"], dtype=object),
            np.array(["snp_jcstj", "snp_dvxkv"], dtype=object),
        )
    ]
    interact_gene = pd.DataFrame(
        [("gene_vcbc", "gene_pipx")], columns=["gene_id_1", "gene_id_2"]
    )

    with pytest.raises(ValueError):
        mk_sparse_isn(snp_data, interact_snp, interact_gene, "pearson", "pool")


def test_on_genes_pearson():
    gene_data = pd.DataFrame(
        [(-100, 50), (11, 20), (22.1, 12.6), (0.1, 0.5), (51.76, 28.42)],
        columns=["gene_vcbc", "gene_pipx"],
    )
    interact = pd.DataFrame([("gene_vcbc", "gene_pipx")], columns=["1", "2"])
    assert_frame_equal(
        mk_sparse_isn(
            gene_data,
            unmapped=None,
            mapped=interact,
            metric="pearson",
        ),
        pd.DataFrame(
            [
                (-6.509092,),
                (-0.638928,),
                (-0.740691,),
                (0.086810,),
                (0.348817,),
            ],
            columns=["gene_vcbc_gene_pipx"],
        ),
    )


def test_on_genes_spearman():
    gene_data = pd.DataFrame(
        [(-100, 50), (11, 20), (22.1, 12.6), (0.1, 0.5), (51.76, 28.42)],
        columns=["gene_vcbc", "gene_pipx"],
    )
    interact = pd.DataFrame([("gene_vcbc", "gene_pipx")], columns=["1", "2"])
    assert_frame_equal(
        mk_sparse_isn(
            gene_data,
            unmapped=None,
            mapped=interact,
            metric="spearman",
        ),
        pd.DataFrame(
            [
                (-3.7,),
                (0.3,),
                (0.3,),
                (1.1,),
                (1.1,),
            ],
            columns=["gene_vcbc_gene_pipx"],
        ),
    )


def test_on_genes_spearman_stack_different_dimensions_bug():
    gene_data = pd.DataFrame(
        [
            (-100, 50, 4),
            (11, 20, 56.34),
            (22.1, 12.6, 234.54),
            (0.1, 0.5, 0.45),
            (51.76, 28.42, 45.0),
        ],
        columns=["gene_vcbc", "gene_pipx", "gene_james"],
    )
    interact = pd.DataFrame(
        [
            ("gene_vcbc", "gene_pipx"),
            ("gene_vcbc", "gene_james"),
            ("gene_james", "gene_pipx"),
            ("gene_james", "gene_james"),
        ],
        columns=["1", "2"],
    )
    assert_frame_equal(
        mk_sparse_isn(
            gene_data,
            unmapped=None,
            mapped=interact,
            metric="spearman",
        ),
        pd.DataFrame(
            [
                (-3.7, 1.4, -0.8, 1.0),
                (0.3, 0.6, -0.8, 1.0),
                (0.3, 0.6, -0.8, 1.0),
                (1.1, 1.4, 4.0, 1.0),
                (1.1, -0.2, -0.8, 1.0),
            ],
            columns=[
                "gene_vcbc_gene_pipx",
                "gene_vcbc_gene_james",
                "gene_james_gene_pipx",
                "gene_james_gene_james",
            ],
            dtype=np.float64,
        ),
    )


def test_spearman_fiddle():
    first = t.tensor(
        [
            [0.1015, 0.0707, 0.1108, 0.6479],
            [0.4688, 0.7204, 0.6506, 0.5650],
            [0.6619, 0.4601, 0.6120, 0.6109],
        ]
    )
    second = t.tensor(
        [
            [0.9352, 0.7916, 0.1136, 0.8020, 0.8635],
            [0.1621, 0.9037, 0.9067, 0.3235, 0.5839],
            [0.1721, 0.7333, 0.0643, 0.2700, 0.6233],
        ]
    )
    res = __spearman_metric(lambda x: x)(first, second)

    assert t.tensor(True) == t.all(
        t.eq(
            res,
            t.tensor(
                [
                    [-0.5000, -0.5000, -0.5000, -1.0000, -0.5000],
                    [-1.0000, 0.5000, 0.5000, -0.5000, -1.0000],
                    [-1.0000, 0.5000, 0.5000, -0.5000, -1.0000],
                    [1.0000, -0.5000, -0.5000, 0.5000, 1.0000],
                ]
            ),
        )
    )


def test_on_genes_dot():
    gene_data = pd.DataFrame(
        [(-100, 50), (11, 20), (22.1, 12.6), (0.1, 0.5), (51.76, 28.42)],
        columns=["gene_vcbc", "gene_pipx"],
    )
    interact = pd.DataFrame([("gene_vcbc", "gene_pipx")], columns=["1", "2"])
    assert_frame_equal(
        mk_sparse_isn(gene_data, unmapped=None, mapped=interact, metric="dot"),
        pd.DataFrame(
            [
                (-23030.4708,),
                (-2150.4708,),
                (-1916.6308,),
                (-3030.2708,),
                (2853.606,),
            ],
            columns=["gene_vcbc_gene_pipx"],
            dtype=np.float32,
        ),
    )


def test_biweight_midcorrelation_simple_no_pooling():
    gene_data = pd.DataFrame(
        [(-100, 50), (11, 20), (22.1, 12.6), (0.1, 0.5), (51.76, 28.42)],
        columns=["gene_vcbc", "gene_pipx"],
    )
    interact = pd.DataFrame([("gene_vcbc", "gene_pipx")], columns=["1", "2"])
    assert_frame_equal(
        mk_sparse_isn(
            gene_data,
            unmapped=None,
            mapped=interact,
            metric="biweight",
        ),
        pd.DataFrame(
            [
                (-0.9460088795964369,),
                (3.6613471049859774,),
                (1.0137487455902223,),
                (0.4770507710323724,),
                (1.2646782579039055,),
            ],
            columns=["gene_vcbc_gene_pipx"],
        ),
    )


def test_biweight_midcorrelation_simple_avg_pooling():
    gene_data = pd.DataFrame(
        [(-100, 50), (11, 20), (22.1, 12.6), (0.1, 0.5), (51.76, 28.42)],
        columns=["gene_vcbc", "gene_pipx"],
    )
    interact = pd.DataFrame([("gene_vcbc", "gene_pipx")], columns=["1", "2"])
    assert_frame_equal(
        mk_sparse_isn(
            gene_data,
            unmapped=None,
            mapped=interact,
            metric="biweight",
            pool="avg",
        ),
        pd.DataFrame(
            [
                (-0.9460088795964369,),
                (3.6613471049859774,),
                (1.0137487455902223,),
                (0.4770507710323724,),
                (1.2646782579039055,),
            ],
            columns=["gene_vcbc_gene_pipx"],
        ),
    )


def test_biweight_midcorrelation_simple_max_pooling():
    gene_data = pd.DataFrame(
        [(-100, 50), (11, 20), (22.1, 12.6), (0.1, 0.5), (51.76, 28.42)],
        columns=["gene_vcbc", "gene_pipx"],
    )
    interact = pd.DataFrame([("gene_vcbc", "gene_pipx")], columns=["1", "2"])
    assert_frame_equal(
        mk_sparse_isn(
            gene_data,
            unmapped=None,
            mapped=interact,
            metric="biweight",
            pool="max",
        ),
        pd.DataFrame(
            [
                (-0.9460088795964369,),
                (3.6613471049859774,),
                (1.0137487455902223,),
                (0.4770507710323724,),
                (1.2646782579039055,),
            ],
            columns=["gene_vcbc_gene_pipx"],
        ),
    )


def test_biweight_midcorrelation_genes_no_pooling():
    gene_data = pd.DataFrame(
        [
            (-100, 50, 4),
            (11, 20, 56.34),
            (22.1, 12.6, 234.54),
            (0.1, 0.5, 0.45),
            (51.76, 28.42, 45.0),
        ],
        columns=["gene_vcbc", "gene_pipx", "gene_james"],
    )
    interact = pd.DataFrame(
        [
            ("gene_vcbc", "gene_pipx"),
            ("gene_vcbc", "gene_james"),
            ("gene_james", "gene_pipx"),
            ("gene_james", "gene_james"),
        ],
        columns=["1", "2"],
    )
    assert_frame_equal(
        mk_sparse_isn(
            gene_data,
            unmapped=None,
            mapped=interact,
            metric="biweight",
        ),
        pd.DataFrame(
            [
                (-0.9460088795964369, 0.5319506129331883, -3.247255229420662, 1.0),
                (3.6613471049859774, 1.4866002751271943, -2.246460644323869, 1.0),
                (1.0137487455902223, np.nan, -3.216540690872173, 1.0),
                (0.4770507710323724, 1.4866002751271943, 2.523214389125642, 1.0),
                (1.2646782579039055, np.nan, -2.5443771131731117, 1.0),
            ],
            columns=[
                "gene_vcbc_gene_pipx",
                "gene_vcbc_gene_james",
                "gene_james_gene_pipx",
                "gene_james_gene_james",
            ],
        ),
    )


def test_biweight_midcorrelation_genes_avg_pooling():
    gene_data = pd.DataFrame(
        [
            (-100, 50, 4),
            (11, 20, 56.34),
            (22.1, 12.6, 234.54),
            (0.1, 0.5, 0.45),
            (51.76, 28.42, 45.0),
        ],
        columns=["gene_vcbc", "gene_pipx", "gene_james"],
    )
    interact = pd.DataFrame(
        [
            ("gene_vcbc", "gene_pipx"),
            ("gene_vcbc", "gene_james"),
            ("gene_james", "gene_pipx"),
            ("gene_james", "gene_james"),
        ],
        columns=["1", "2"],
    )
    assert_frame_equal(
        mk_sparse_isn(
            gene_data,
            unmapped=None,
            mapped=interact,
            metric="biweight",
            pool="avg",
        ),
        pd.DataFrame(
            [
                (-0.9460088795964369, 0.5319506129331883, -3.247255229420662, 1.0),
                (3.6613471049859774, 1.4866002751271943, -2.246460644323869, 1.0),
                (1.0137487455902223, np.nan, -3.216540690872173, 1.0),
                (0.4770507710323724, 1.4866002751271943, 2.523214389125642, 1.0),
                (1.2646782579039055, np.nan, -2.5443771131731117, 1.0),
            ],
            columns=[
                "gene_vcbc_gene_pipx",
                "gene_vcbc_gene_james",
                "gene_james_gene_pipx",
                "gene_james_gene_james",
            ],
        ),
    )


def test_biweight_midcorrelation_genes_max_pooling():
    gene_data = pd.DataFrame(
        [
            (-100, 50, 4),
            (11, 20, 56.34),
            (22.1, 12.6, 234.54),
            (0.1, 0.5, 0.45),
            (51.76, 28.42, 45.0),
        ],
        columns=["gene_vcbc", "gene_pipx", "gene_james"],
    )
    interact = pd.DataFrame(
        [
            ("gene_vcbc", "gene_pipx"),
            ("gene_vcbc", "gene_james"),
            ("gene_james", "gene_pipx"),
            ("gene_james", "gene_james"),
        ],
        columns=["1", "2"],
    )
    assert_frame_equal(
        mk_sparse_isn(
            gene_data,
            unmapped=None,
            mapped=interact,
            metric="biweight",
            pool="max",
        ),
        pd.DataFrame(
            [
                (-0.9460088795964369, 0.5319506129331883, -3.247255229420662, 1.0),
                (3.6613471049859774, 1.4866002751271943, -2.246460644323869, 1.0),
                (1.0137487455902223, np.nan, -3.216540690872173, 1.0),
                (0.4770507710323724, 1.4866002751271943, 2.523214389125642, 1.0),
                (1.2646782579039055, np.nan, -2.5443771131731117, 1.0),
            ],
            columns=[
                "gene_vcbc_gene_pipx",
                "gene_vcbc_gene_james",
                "gene_james_gene_pipx",
                "gene_james_gene_james",
            ],
        ),
    )


def test_biweight_midcorrelation_snp_no_pooling():
    snp_data = pd.DataFrame(
        [(1, 1, 2, 1), (1, 2, 2, 0), (2, 1, 0, 2), (0, 2, 1, 2), (1, 2, 0, 1)],
        columns=["snp_a", "snp_b", "snp_c", "snp_d"],
    )
    interact_snp = [
        (
            np.array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
            np.array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
        ),
        (
            np.array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
            np.array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
        ),
        (
            np.array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
            np.array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
        ),
        (
            np.array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
            np.array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
        ),
    ]
    interact_gene = pd.DataFrame(
        [
            ("gene_a", "gene_b"),
            ("gene_a", "gene_c"),
            ("gene_b", "gene_c"),
            ("gene_c", "gene_d"),
        ],
        columns=["gene_id_1", "gene_id_2"],
    )

    computed = mk_sparse_isn(
        snp_data,
        interact_snp,
        interact_gene,
        metric="biweight",
    )

    assert_frame_equal(
        computed,
        pd.DataFrame(
            [
                (1.0, 1.0, 1.0, 1.0),
                (1.0, 1.0, 1.0, 1.0),
                (1.0, 1.0, 1.0, 1.0),
                (1.0, 1.0, 1.0, 1.0),
                (1.0, 1.0, 1.0, 1.0),
            ],
            columns=[
                "gene_a_gene_b",
                "gene_a_gene_c",
                "gene_b_gene_c",
                "gene_c_gene_d",
            ],
            dtype=np.float32,
        ),
    )


def test_biweight_midcorrelation_snp_avg_pooling():
    snp_data = pd.DataFrame(
        [(1, 1, 2, 1), (1, 2, 2, 0), (2, 1, 0, 2), (0, 2, 1, 2), (1, 2, 0, 1)],
        columns=["snp_a", "snp_b", "snp_c", "snp_d"],
    )
    interact_snp = [
        (
            np.array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
            np.array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
        ),
        (
            np.array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
            np.array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
        ),
        (
            np.array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
            np.array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
        ),
        (
            np.array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
            np.array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
        ),
    ]
    interact_gene = pd.DataFrame(
        [
            ("gene_a", "gene_b"),
            ("gene_a", "gene_c"),
            ("gene_b", "gene_c"),
            ("gene_c", "gene_d"),
        ],
        columns=["gene_id_1", "gene_id_2"],
    )

    computed = mk_sparse_isn(
        snp_data,
        interact_snp,
        interact_gene,
        metric="biweight",
        pool="avg",
    )

    assert_frame_equal(
        computed,
        pd.DataFrame(
            [
                (1.0, 1.0, 1.0, 1.0),
                (1.0, 1.0, 1.0, 1.0),
                (1.0, 1.0, 1.0, 1.0),
                (1.0, 1.0, 1.0, 1.0),
                (1.0, 1.0, 1.0, 1.0),
            ],
            columns=[
                "gene_a_gene_b",
                "gene_a_gene_c",
                "gene_b_gene_c",
                "gene_c_gene_d",
            ],
            dtype=np.float32,
        ),
    )


def test_biweight_midcorrelation_snp_max_pooling():
    snp_data = pd.DataFrame(
        [(1, 1, 2, 1), (1, 2, 2, 0), (2, 1, 0, 2), (0, 2, 1, 2), (1, 2, 0, 1)],
        columns=["snp_a", "snp_b", "snp_c", "snp_d"],
    )
    interact_snp = [
        (
            np.array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
            np.array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
        ),
        (
            np.array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
            np.array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
        ),
        (
            np.array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
            np.array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
        ),
        (
            np.array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
            np.array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
        ),
    ]
    interact_gene = pd.DataFrame(
        [
            ("gene_a", "gene_b"),
            ("gene_a", "gene_c"),
            ("gene_b", "gene_c"),
            ("gene_c", "gene_d"),
        ],
        columns=["gene_id_1", "gene_id_2"],
    )

    computed = mk_sparse_isn(
        snp_data,
        interact_snp,
        interact_gene,
        metric="biweight",
        pool="max",
    )

    assert_frame_equal(
        computed,
        pd.DataFrame(
            [
                (1.0, 1.0, 1.0, 1.0),
                (1.0, 1.0, 1.0, 1.0),
                (1.0, 1.0, 1.0, 1.0),
                (1.0, 1.0, 1.0, 1.0),
                (1.0, 1.0, 1.0, 1.0),
            ],
            columns=[
                "gene_a_gene_b",
                "gene_a_gene_c",
                "gene_b_gene_c",
                "gene_c_gene_d",
            ],
            dtype=np.float32,
        ),
    )


def test_dense():
    gene_data = pd.DataFrame(
        [
            (0.162634, 0.449745, 0.968108),
            (0.409558, 0.092939, 0.284362),
            (0.755906, 0.189236, 0.774311),
        ],
        columns=["gene1", "gene2", "gene3"],
    )

    out_columns = [
        "gene1_gene1",
        "gene1_gene2",
        "gene1_gene3",
        "gene2_gene1",
        "gene2_gene2",
        "gene2_gene3",
        "gene3_gene1",
        "gene3_gene2",
        "gene3_gene3",
    ]

    expected = pd.DataFrame(
        [
            (
                1.0,
                -3.9023278,
                -2.543286,
                -3.9023278,
                1.0,
                0.625879,
                -2.543286,
                0.625879,
                1.0,
            ),
            (
                1.0,
                0.0976758,
                1.456714,
                0.0976758,
                1.0,
                0.625879,
                1.456714,
                0.625879,
                1.0,
            ),
            (
                1.0,
                0.09767747,
                1.456714,
                0.09767747,
                1.0,
                0.625879,
                1.456714,
                0.625879,
                1.0,
            ),
        ],
        columns=out_columns,
    )

    for x in expected.columns:
        expected[x] = expected[x].astype(np.float32)

    new = pd.DataFrame(
        [network.numpy().astype(np.float32) for network in dense_isn(gene_data.copy())],
        columns=out_columns,
    )
    assert_frame_equal(expected, new, rtol=0.00001, atol=0.00001)


def test_dense_offline():
    gene_data = pd.DataFrame(
        [
            (0.162634, 0.449745, 0.968108),
            (0.409558, 0.092939, 0.284362),
            (0.755906, 0.189236, 0.774311),
            (0.834372, 0.159229, 0.475373),
            (0.449133, 0.562913, 0.956922),
        ],
        columns=["gene1", "gene2", "gene3"],
    )

    out_columns = [
        "gene1_gene1",
        "gene1_gene2",
        "gene1_gene3",
        "gene2_gene1",
        "gene2_gene2",
        "gene2_gene3",
        "gene3_gene1",
        "gene3_gene2",
        "gene3_gene3",
    ]

    online = pd.DataFrame(
        [network.numpy().astype(np.float32) for network in dense_isn(gene_data.copy())],
        columns=out_columns,
    )

    # offline = pd.DataFrame(dense_isn_offline(gene_data.copy()), columns=out_columns)
    offline = pd.DataFrame(
        [network.numpy() for network in dense_isn_offline(gene_data.copy())],
        columns=out_columns,
    )

    assert_frame_equal(online, offline, rtol=0.00001, atol=0.00001)
