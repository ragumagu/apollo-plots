import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter, FuncFormatter

from font_settings import load_iso_font

load_iso_font()

fig = plt.figure(figsize=(5.5, 4), dpi=80)
ax = fig.add_subplot(111)
ax.spines[['right', 'top']].set_visible(False)

ax.set_xlim(10, 2000)
ax.set_ylim(.001, .1)
ax.tick_params(axis="x", direction="in")
ax.tick_params(axis="y", direction="in")
ax.tick_params(axis="x", which="minor", direction="in")
ax.tick_params(axis="y", which="minor", direction="in")

ax.plot([20, 80, 350, 2000], [.01, .04, .04, .01], color="black")

ax.set_yscale('log')
ax.set_yticks([.1, .08, .06, .04, .02, .01, .008, .006, .004, .002, .001])

# Using %g for formatting the float
# Using [1:] to drop the leading zero
ax.get_yaxis().set_major_formatter(FuncFormatter(lambda x, y: (str(x).format("%g"))[1:]))

ax.set_xscale('log')
ax.set_xticks([10, 20, 40, 60, 100, 200, 400, 600, 1000, 2000])

ax.get_xaxis().set_major_formatter(ScalarFormatter())

ax.set_ylabel(r"POWER SPECTRAL"
              "\n"
              r"DENSITY, $\mathregular{g^2/Hz}$", rotation='horizontal', ha='right')
ax.set_xlabel("FREQUENCY, Hz")

title = "Figure 1-1. - Vibration test level for acceptance."
plt.title(title, y=-0.4)

fig.tight_layout()

plt.show()
