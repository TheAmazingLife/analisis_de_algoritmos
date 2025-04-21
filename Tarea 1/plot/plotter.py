import matplotlib.pyplot as plt
import pandas as pd

log_log = pd.read_csv("experimental_data/log-log_ms.csv")
cool = pd.read_csv("experimental_data/cool_ms.csv")
semi_log = pd.read_csv("experimental_data/semi-log_ns.csv")

fig, ax = plt.subplots(1, 3)

ax[0].errorbar(
    log_log["n"],
    log_log["t_mean"],
    log_log["t_stdev"],
    linestyle="None",
    marker='.',
    ecolor='tab:red'
)

ax[0].set_title("log-log")
ax[0].set_xlabel("x axis label")
ax[0].set_ylabel("y axis label")
ax[0].set_xscale("log")
ax[0].set_yscale("log")

ax[1].errorbar(
    cool["p"],
    cool["t_mean"],
    cool["t_stdev"],
    linestyle="None",
    marker='.',
    ecolor='tab:red'
)

ax[1].set_title("Super cool and descriptive name")
ax[1].set_xlabel("Unit length variable")
ax[1].set_ylabel("Response")

ax[2].errorbar(
    semi_log["p"],
    semi_log["t_mean"],
    semi_log["t_stdev"],
    linestyle="None",
    marker='.',
    ecolor='tab:red'
)

ax[2].set_title("semi-log plot")
ax[2].set_xlabel("Positions")
ax[2].set_ylabel("Average happiness")
ax[2].set_xscale("log", base=2)

fig.tight_layout()
fig.savefig("sample_plots.png")
