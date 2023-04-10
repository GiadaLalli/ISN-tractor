import pytest
from isn_tractor.ibisn import sparse_isn, __spearman_metric

from numpy import array, zeros
import pandas as pd
from pandas.testing import assert_frame_equal
from sklearn.metrics import normalized_mutual_info_score as mutual_info
import torch as t


def my_mutual_info_metric(first, second):
    first = t.tensor(first)
    second = t.tensor(second)
    if (first.dim(), second.dim()) == (1, 1):
        return mutual_info(first, second)

    scores = t.zeros((first.shape[1], second.shape[1]))
    for i in range(first.shape[1]):
        for j in range(second.shape[1]):
            scores[i, j] = mutual_info(first[:, i], second[:, j])
    return scores


def test_empty_inputs():
    snp_data = pd.DataFrame()
    interact_snp = []
    interact_gene = pd.DataFrame()
    with pytest.raises(ValueError):
        sparse_isn(snp_data, interact_snp, interact_gene, "pearson", "avg"),


def test_snp_pearson_avg():
    snp_data = pd.DataFrame(
        [(1, 0), (1, 2), (2, 1), (0, 0), (1, 2)], columns=["snp_jcstj", "snp_dvxkv"]
    )
    interact_snp = [
        (
            array(["snp_jcstj", "snp_dvxkv"], dtype=object),
            array(["snp_jcstj", "snp_dvxkv"], dtype=object),
        )
    ]
    interact_gene = pd.DataFrame(
        [("gene_vcbc", "gene_pipx")], columns=["gene_id_1", "gene_id_2"]
    )
    assert_frame_equal(
        sparse_isn(snp_data, interact_snp, interact_gene, "pearson", "avg"),
        pd.DataFrame(
            [
                (0.531081,),
                (0.531081,),
                (0.229183,),
                (1.732039,),
                (0.531081,),
            ],
            columns=["gene_vcbc_gene_pipx"],
        ),
    )


def test_snp_pearson_max():
    snp_data = pd.DataFrame(
        [(1, 0), (1, 2), (2, 1), (0, 0), (1, 2)], columns=["snp_jcstj", "snp_dvxkv"]
    )
    interact_snp = [
        (
            array(["snp_jcstj", "snp_dvxkv"], dtype=object),
            array(["snp_jcstj", "snp_dvxkv"], dtype=object),
        )
    ]
    interact_gene = pd.DataFrame(
        [("gene_vcbc", "gene_pipx")], columns=["gene_id_1", "gene_id_2"]
    )
    assert_frame_equal(
        sparse_isn(snp_data, interact_snp, interact_gene, "pearson", "max"),
        pd.DataFrame(
            [
                (1.0,),
                (1.0,),
                (1.0,),
                (1.0,),
                (1.0,),
            ],
            columns=["gene_vcbc_gene_pipx"],
        ),
    )


def test_snp_spearman_avg():
    snp_data = pd.DataFrame(
        [(1, 0), (1, 2), (2, 1), (0, 0), (1, 2)], columns=["snp_jcstj", "snp_dvxkv"]
    )
    interact_snp = [
        (
            array(["snp_jcstj", "snp_dvxkv"], dtype=object),
            array(["snp_jcstj", "snp_dvxkv"], dtype=object),
        )
    ]
    interact_gene = pd.DataFrame(
        [("gene_vcbc", "gene_pipx")], columns=["gene_id_1", "gene_id_2"]
    )
    assert_frame_equal(
        sparse_isn(snp_data, interact_snp, interact_gene, "spearman", "avg"),
        pd.DataFrame(
            [
                (0.717217,),
                (0.383883,),
                (0.229183,),
                (1.928214,),
                (0.383883,),
            ],
            columns=["gene_vcbc_gene_pipx"],
        ),
    )


def test_snp_spearman_max():
    snp_data = pd.DataFrame(
        [(1, 0), (1, 2), (2, 1), (0, 0), (1, 2)], columns=["snp_jcstj", "snp_dvxkv"]
    )
    interact_snp = [
        (
            array(["snp_jcstj", "snp_dvxkv"], dtype=object),
            array(["snp_jcstj", "snp_dvxkv"], dtype=object),
        )
    ]
    interact_gene = pd.DataFrame(
        [("gene_vcbc", "gene_pipx")], columns=["gene_id_1", "gene_id_2"]
    )
    assert_frame_equal(
        sparse_isn(snp_data, interact_snp, interact_gene, "spearman", "max"),
        pd.DataFrame(
            [
                (1.0,),
                (1.0,),
                (1.0,),
                (1.0,),
                (1.0,),
            ],
            columns=["gene_vcbc_gene_pipx"],
        ),
    )


def test_snp_mutual_info_avg():
    snp_data = pd.DataFrame(
        [(1, 0), (1, 2), (2, 1), (0, 0), (1, 2)], columns=["snp_jcstj", "snp_dvxkv"]
    )
    interact_snp = [
        (
            array(["snp_jcstj", "snp_dvxkv"], dtype=object),
            array(["snp_jcstj", "snp_dvxkv"], dtype=object),
        )
    ]
    interact_gene = pd.DataFrame(
        [("gene_vcbc", "gene_pipx")], columns=["gene_id_1", "gene_id_2"]
    )
    assert_frame_equal(
        sparse_isn(snp_data, interact_snp, interact_gene, my_mutual_info_metric, "avg"),
        pd.DataFrame(
            [
                (0.178174,),
                (0.844840,),
                (1.490751,),
                (0.77414,),
                (0.844840,),
            ],
            columns=["gene_vcbc_gene_pipx"],
        ),
    )


def test_snp_mutual_info_max():
    snp_data = pd.DataFrame(
        [(1, 0), (1, 2), (2, 1), (0, 0), (1, 2)], columns=["snp_jcstj", "snp_dvxkv"]
    )
    interact_snp = [
        (
            array(["snp_jcstj", "snp_dvxkv"], dtype=object),
            array(["snp_jcstj", "snp_dvxkv"], dtype=object),
        )
    ]
    interact_gene = pd.DataFrame(
        [("gene_vcbc", "gene_pipx")], columns=["gene_id_1", "gene_id_2"]
    )
    assert_frame_equal(
        sparse_isn(snp_data, interact_snp, interact_gene, my_mutual_info_metric, "max"),
        pd.DataFrame(
            [
                (1.0,),
                (1.0,),
                (1.0,),
                (1.0,),
                (1.0,),
            ],
            columns=["gene_vcbc_gene_pipx"],
        ),
    )


def test_snp_dot_avg():
    snp_data = pd.DataFrame(
        [(1, 0), (1, 2), (2, 1), (0, 0), (1, 2)], columns=["snp_jcstj", "snp_dvxkv"]
    )
    interact_snp = [
        (
            array(["snp_jcstj", "snp_dvxkv"], dtype=object),
            array(["snp_jcstj", "snp_dvxkv"], dtype=object),
        )
    ]
    interact_gene = pd.DataFrame(
        [("gene_vcbc", "gene_pipx")], columns=["gene_id_1", "gene_id_2"]
    )
    assert_frame_equal(
        sparse_isn(snp_data, interact_snp, interact_gene, "dot", "avg"),
        pd.DataFrame(
            [
                (8.0,),
                (16.0,),
                (16.0,),
                (7.0,),
                (16.0,),
            ],
            columns=["gene_vcbc_gene_pipx"],
        ),
    )


def test_snp_dot_max():
    snp_data = pd.DataFrame(
        [(1, 0), (1, 2), (2, 1), (0, 0), (1, 2)], columns=["snp_jcstj", "snp_dvxkv"]
    )
    interact_snp = [
        (
            array(["snp_jcstj", "snp_dvxkv"], dtype=object),
            array(["snp_jcstj", "snp_dvxkv"], dtype=object),
        )
    ]
    interact_gene = pd.DataFrame(
        [("gene_vcbc", "gene_pipx")], columns=["gene_id_1", "gene_id_2"]
    )
    assert_frame_equal(
        sparse_isn(snp_data, interact_snp, interact_gene, "dot", "max"),
        pd.DataFrame(
            [
                (9.0,),
                (21.0,),
                (13.0,),
                (9.0,),
                (21.0,),
            ],
            columns=["gene_vcbc_gene_pipx"],
        ),
    )


def test_snp_larger():
    snp_data = pd.DataFrame(
        [(1, 0, 1, 1), (1, 2, 2, 0), (2, 1, 0, 2), (0, 0, 1, 0), (1, 2, 0, 0)],
        columns=["snp_a", "snp_b", "snp_c", "snp_d"],
    )
    interact_snp = [
        (
            array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
            array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
        ),
        (
            array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
            array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
        ),
        (
            array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
            array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
        ),
        (
            array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
            array(["snp_a", "snp_b", "snp_c", "snp_d"], dtype=object),
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

    computed = sparse_isn(snp_data, interact_snp, interact_gene, "pearson", "average")
    print(computed, flush=True)

    assert_frame_equal(
        computed,
        pd.DataFrame(
            [
                (0.1098762, 0.1098762, 0.1098762, 0.1098762),
                (0.847243, 0.8472431, 0.8472431, 0.8472431),
                (-0.0930169, -0.0930169, -0.0930169, -0.0930169),
                (0.6876522, 0.6876522, 0.6876522, 0.6876522),
                (0.0056454, 0.0056454, 0.0056454, 0.0056454),
            ],
            columns=[
                "gene_a_gene_b",
                "gene_a_gene_c",
                "gene_b_gene_c",
                "gene_c_gene_d",
            ],
        ),
    )


def test_invalid_metric_without_data():
    snp_data = pd.DataFrame()
    interact_snp = []
    interact_gene = pd.DataFrame()

    with pytest.raises(ValueError):
        sparse_isn(snp_data, interact_snp, interact_gene, "metric", "avg")


def test_invalid_metric_with_data():
    snp_data = pd.DataFrame(
        [(1, 0), (1, 2), (2, 1), (0, 0), (1, 2)], columns=["snp_jcstj", "snp_dvxkv"]
    )
    interact_snp = [
        (
            array(["snp_jcstj", "snp_dvxkv"], dtype=object),
            array(["snp_jcstj", "snp_dvxkv"], dtype=object),
        )
    ]
    interact_gene = pd.DataFrame(
        [("gene_vcbc", "gene_pipx")], columns=["gene_id_1", "gene_id_2"]
    )

    with pytest.raises(ValueError):
        sparse_isn(snp_data, interact_snp, interact_gene, "metric", "avg")


def test_invalid_pool_without_data():
    snp_data = pd.DataFrame()
    interact_snp = []
    interact_gene = pd.DataFrame()

    with pytest.raises(ValueError):
        sparse_isn(snp_data, interact_snp, interact_gene, "pearson", "pool")


def test_invalid_pool_with_data():
    snp_data = pd.DataFrame(
        [(1, 0), (1, 2), (2, 1), (0, 0), (1, 2)], columns=["snp_jcstj", "snp_dvxkv"]
    )
    interact_snp = [
        (
            array(["snp_jcstj", "snp_dvxkv"], dtype=object),
            array(["snp_jcstj", "snp_dvxkv"], dtype=object),
        )
    ]
    interact_gene = pd.DataFrame(
        [("gene_vcbc", "gene_pipx")], columns=["gene_id_1", "gene_id_2"]
    )

    with pytest.raises(ValueError):
        sparse_isn(snp_data, interact_snp, interact_gene, "pearson", "pool")


def test_on_genes_pearson():
    gene_data = pd.DataFrame(
        [(-100, 50), (11, 20), (22.1, 12.6), (0.1, 0.5), (51.76, 28.42)],
        columns=["gene_vcbc", "gene_pipx"],
    )
    interact = pd.DataFrame([("gene_vcbc", "gene_pipx")], columns=["1", "2"])
    assert_frame_equal(
        sparse_isn(
            gene_data,
            interact_unmapped=None,
            interact_mapped=interact,
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
    print(sparse_isn(gene_data, interact_unmapped=None, interact_mapped=interact, metric="spearman"))
    assert_frame_equal(
        sparse_isn(
            gene_data,
            interact_unmapped=None,
            interact_mapped=interact,
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
        sparse_isn(
            gene_data,
            interact_unmapped=None,
            interact_mapped=interact,
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
    res = __spearman_metric(first, second)
    print(res)
    assert t.tensor(True) == t.all(
        t.eq(
            res,
            t.tensor(
                [
                    [-0.5000, -0.5000, -0.5000, -1.0000, -0.5000],
                    [-1.0000,  0.5000,  0.5000, -0.5000, -1.0000],
                    [-1.0000,  0.5000,  0.5000, -0.5000, -1.0000],
		    [ 1.0000, -0.5000, -0.5000,  0.5000,  1.0000],
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
        sparse_isn(
            gene_data, interact_unmapped=None, interact_mapped=interact, metric="dot"
        ),
        pd.DataFrame(
            [
                (-23030.4708,),
                (-2150.4708,),
                (-1916.6308,),
                (-3030.2708,),
                (2853.606,),
            ],
            columns=["gene_vcbc_gene_pipx"],
        ),
    )
