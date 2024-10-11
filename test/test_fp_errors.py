import pytest

import pandas as pd
from pandas.testing import assert_frame_equal

from isn_tractor.ibisn import dense_isn
from benchmark.benchmark import continuous
from benchmark.dense_isn_offline import dense_isn_offline

def test_10_20():
    data = continuous(10, 20)
    online = pd.DataFrame(isn.numpy() for isn in dense_isn(data))
    offline = pd.DataFrame(isn.numpy() for isn in dense_isn_offline(data))
    assert_frame_equal(online, offline)

def test_25_50():
    data = continuous(25, 50)
    online = pd.DataFrame(isn.numpy() for isn in dense_isn(data))
    offline = pd.DataFrame(isn.numpy() for isn in dense_isn_offline(data))
    assert_frame_equal(online, offline)

def test_100_200():
    data = continuous(100, 200)
    online = pd.DataFrame(isn.numpy() for isn in dense_isn(data))
    offline = pd.DataFrame(isn.numpy() for isn in dense_isn_offline(data))
    assert_frame_equal(online, offline)
