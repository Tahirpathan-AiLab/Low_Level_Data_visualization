import matplotlib.pyplot as plt

# Figure settings
plt.rcParams["figure.figsize"] = (12, 6)
plt.rcParams["figure.dpi"] = 100

# Font settings
plt.rcParams["font.size"] = 12
plt.rcParams["axes.titlesize"] = 16
plt.rcParams["axes.labelsize"] = 13
plt.rcParams["xtick.labelsize"] = 11
plt.rcParams["ytick.labelsize"] = 11

# Line settings
plt.rcParams["lines.linewidth"] = 2.5
plt.rcParams["lines.markersize"] = 6

# Grid settings
plt.rcParams["axes.grid"] = True
plt.rcParams["grid.alpha"] = 0.3
plt.rcParams["grid.linestyle"] = "--"

# Legend settings
plt.rcParams["legend.fontsize"] = 11
plt.rcParams["legend.frameon"] = True

# Axes settings
plt.rcParams["axes.spines.top"] = False
plt.rcParams["axes.spines.right"] = False

# Save figure settings
plt.rcParams["savefig.dpi"] = 300
plt.rcParams["savefig.bbox"] = "tight"