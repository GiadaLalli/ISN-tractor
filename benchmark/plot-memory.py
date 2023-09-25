from matplotlib import pyplot as plt
import pandas as pd

fig = plt.figure()
gs = fig.add_gridspec(1, 4, wspace=0)
axs = gs.subplots(sharex=True, sharey=True)
for i, sample_size in enumerate([50, 100, 200, 500]):
    df = pd.read_csv(f"memory-stats/memory-{sample_size}.csv")
    df /= 1000000
    ax = df.boxplot(ax=axs[i])
    ax.label_outer()
    axs[i].title.set_text(f"{sample_size} samples")

fig.text(0.5, 0.04, "Number of features", ha="center")
fig.text(0.04, 0.5, "Memory usage (GiB)", va="center", rotation="vertical")
plt.savefig("memory-stats/tractor.png")

fig.clf()
fig = plt.figure()
gs = fig.add_gridspec(1, 4, wspace=0)
axs = gs.subplots(sharex=True, sharey=True)
for i, sample_size in enumerate([50, 100, 200, 500]):
    df = pd.read_csv(f"memory-stats/R-memory-{sample_size}.csv")
    df /= 1000000
    ax = df.boxplot(ax=axs[i])
    ax.label_outer()
    axs[i].title.set_text(f"{sample_size} samples")

fig.text(0.5, 0.04, "Number of features", ha="center")
fig.text(0.04, 0.5, "Memory usage (GiB)", va="center", rotation="vertical")
plt.savefig("memory-stats/lionessR.png")
