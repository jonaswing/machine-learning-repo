from matplotlib import pyplot as plt
import matplotlib.ticker as ticker


fig, axd = plt.subplot_mosaic([["A", ".", "B", "B", ".", "C"],
                               ["A", ".", "B", "B", ".", "C"],
                               [".", ".", ".", ".", ".", "."],
                               ["D", "D", ".", ".", "E", "E"]])


axd["A"].plot()
axd["B"].plot()
axd["C"].plot()
axd["D"].plot()
axd["E"].plot()


for key, ax in axd.items():
    ax.set_xticks([0, 0.5, 1])
    ax.set_xticklabels(["0", "0.5", "1"])
    ax.set_ylim(0, 1)
    if key in ["D", "E"]:
        ax.yaxis.set_major_locator(ticker.FixedLocator([0, 0.5, 1]))
    else:
        ax.yaxis.set_major_locator(ticker.MaxNLocator(6))
    if key != ".":  # Adjust x-axis limits for all axes except "A"
        ax.set_xlim(left=0)


plt.show()


