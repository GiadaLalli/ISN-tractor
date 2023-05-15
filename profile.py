import torch
from torch.profiler import profile, record_function, ProfilerActivity
import isn_tractor.ibisn as it
from benchmark import continuous

df = continuous(200, 1000)

with profile(
    activities=[ProfilerActivity.CPU], record_shapes=True, profile_memory=True
) as prof:
    it.dense_isn(df)

print(
    prof.key_averages(group_by_input_shape=True).table(
        sort_by="cpu_time_total", row_limit=10
    )
)
print(prof.key_averages().table(sort_by="cpu_memory_usage", row_limit=10))
