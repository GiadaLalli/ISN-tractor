import cProfile
from pstats import SortKey

from torch.profiler import profile, record_function, ProfilerActivity
import isn_tractor.ibisn as it
from benchmark import continuous, interactions

print("Initialising inputs...", end="", flush=True)
df = continuous(100, 200)
interact = interactions(200)
print("[DONE]", flush=True)


def run_benchmark():
    with profile(
        activities=[ProfilerActivity.CPU],
        record_shapes=True,
        profile_memory=False,
    ) as prof:
        with record_function("Biweight midcorrelation"):
            for isn in it.sparse_isn(df, None, interact, "biweight", "avg"):
                del isn

    # print(
    #     prof.key_averages(group_by_input_shape=True).table(
    #         sort_by="cpu_time_total", row_limit=10
    #     )
    # )
    # print(
    #   prof.key_averages(group_by_input_shape=True).table(
    #       sort_by="cpu_memory_usage", row_limit=25
    #   )
    # )

    prof.export_chrome_trace("profiling_trace.json")

    # prof.export_stacks("profiler_stacks.txt", "self_cpu_time_total")


if __name__ == "__main__":
    # run_benchmark()
    with cProfile.Profile() as pr:
        for isn in it.sparse_isn(df, None, interact, "biweight", "max"):
            del isn
        pr.print_stats(SortKey.CUMULATIVE)
        # print()
        # next(it.sparse_isn(df, None, interact, "biweight_midcorrelation"))
