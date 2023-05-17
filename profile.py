import torch
from torch.profiler import profile, record_function, ProfilerActivity
import isn_tractor.ibisn as it
from benchmark import continuous

df = continuous(500, 1500)

with profile(
    activities=[ProfilerActivity.CPU],
    record_shapes=True,
    profile_memory=True,
    with_stack=True,
) as prof:
    for isn in it.dense_isn(df):
        del isn

print(
    prof.key_averages(group_by_input_shape=True).table(
        sort_by="cpu_time_total", row_limit=25
    )
)
print(
    prof.key_averages(group_by_input_shape=True).table(
        sort_by="cpu_memory_usage", row_limit=25
    )
)

prof.export_chrome_trace("profiling_trace.json")

prof.export_stacks("profiler_stacks.txt", "self_cpu_time_total")
