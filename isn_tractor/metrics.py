"""
Some assorted metrics for ISN-tractor
"""

import allel
from sklearn.metrics import normalized_mutual_info_score as mutual_info
import torch as t
from torchmetrics import SpearmanCorrCoef, PearsonCorrCoef, R2Score


def pearson_metric_t(first: t.Tensor, second: t.Tensor):
    "TODO:"
    if (first.dim(), second.dim()) == (1, 1):
        return t.corrcoef(t.tensor(first, second))[
            0, 1
        ]  # TODO: I have no idea what you're doing here

    combined = t.cat([first, second], dim=1)
    return t.corrcoef(combined.T)[: first.shape[1] - 1, first.shape[1] :]


def pearson_corr_tm(first: t.Tensor, second: t.Tensor) -> float:
    "TODO:"
    # Reshape both tensors to 1D
    first_flat = first.reshape(-1)
    second_flat = second.reshape(-1)

    # Pad the smaller tensor with zeros if needed to match the length of the larger tensor
    if len(first_flat) > len(second_flat):
        second_flat = t.cat([second_flat, t.zeros(len(first_flat) - len(second_flat))])
    else:
        first_flat = t.cat([first_flat, t.zeros(len(second_flat) - len(first_flat))])

    # Compute the spearman correlation score
    pearson = PearsonCorrCoef()
    score = pearson(first_flat, second_flat)
    return score.item()


def spearman_metric_t(first: t.Tensor, second: t.Tensor):
    "TODO:"
    if (first.dim(), second.dim()) == (1, 1):
        first_sorted = t.argsort(first)
        second_sorted = t.argsort(second)
        combined = t.cat((first_sorted, second_sorted), dim=1)
        return t.corrcoef(combined.T)[0, 1]

    first_sorted = t.argsort(first, dim=0)
    second_sorted = t.argsort(second, dim=0)
    combined = t.cat((first_sorted, second_sorted), dim=1)
    return t.corrcoef(combined.T)[: first.shape[1] - 1, first.shape[1] :]


def spearman_score_tm(first: t.Tensor, second: t.Tensor) -> float:
    "TODO:"
    # Reshape both tensors to 1D
    first_flat = first.reshape(-1)
    second_flat = second.reshape(-1)

    # Pad the smaller tensor with zeros if needed to match the length of the larger tensor
    if len(first_flat) > len(second_flat):
        second_flat = t.cat([second_flat, t.zeros(len(first_flat) - len(second_flat))])
    else:
        first_flat = t.cat([first_flat, t.zeros(len(second_flat) - len(first_flat))])

    # Compute the spearman correlation score
    spearman = SpearmanCorrCoef()
    score = spearman(first_flat, second_flat)
    return score.item()


def linkdis_metric_t(first, second):
    "TODO:"
    first = t.tensor(first)
    second = t.tensor(second)
    scores = allel.rogers_huff_r_between(first.T, second.T)
    scores = t.square(t.from_numpy(scores))
    score = t.mean(scores)
    return score.item()


def r2_score_tm(first: t.Tensor, second: t.Tensor) -> float:
    "TODO:"
    # Reshape both tensors to 1D
    first_flat = first.reshape(-1)
    second_flat = second.reshape(-1)

    # Pad the smaller tensor with zeros if needed to match the length of the larger tensor
    if len(first_flat) > len(second_flat):
        second_flat = t.cat([second_flat, t.zeros(len(first_flat) - len(second_flat))])
    else:
        first_flat = t.cat([first_flat, t.zeros(len(second_flat) - len(first_flat))])

    # Compute the spearman correlation score
    r2score = R2Score()
    score = r2score(first_flat, second_flat)
    return score.item()


def mutualinfo_metric_t(first: t.Tensor, second: t.Tensor):
    "TODO:"
    if (first.dim(), second.dim()) == (1, 1):
        return mutual_info(first, second)

    scores = t.zeros((first.shape[1], second.shape[1]))
    for i in range(first.shape[1]):
        for j in range(second.shape[1]):
            scores[i, j] = mutual_info(first[:, i], second[:, j])
    return scores.numpy()


def dot_metric_t(first: t.Tensor, second: t.Tensor):
    "TODO:"
    return t.matmul(first.permute(*t.arange(first.ndim - 1, -1, -1)), second).numpy()
