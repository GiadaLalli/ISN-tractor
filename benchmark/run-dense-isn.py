import sys

from benchmark import continuous
from isn_tractor.ibisn import dense_isn

sample_size = sys.argv[1]
variables = sys.argv[2]
df = continuous(int(sample_size), int(variables))

for isn in dense_isn(df):
    del isn
