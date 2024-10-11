"""Implementation of the offline LionessR algorithm using an offline Pearson metric."""

import torch as t
from numpy import float64


def dense_isn_offline(data, device=None):
    """Lionessr using offline pearson metric."""
    xt = t.tensor(data.T.to_numpy(dtype=float64, copy=False), device=device)
    nrsamples = xt.size(1)

    net = t.corrcoef(xt)
    agg = net.flatten()

    for i in range(nrsamples):
        ss = t.corrcoef(t.cat((xt[:, :i], xt[:, i + 1 :]), dim=1)).flatten()
        yield nrsamples * (agg - ss) + ss

