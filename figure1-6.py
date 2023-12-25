import matplotlib.pyplot as plt
import numpy as np

from font_settings import load_iso_font

load_iso_font()

fig = plt.figure(figsize=(5, 4.5), dpi=80)
ax = fig.add_subplot(111)

ax.spines[['right', 'top']].set_visible(False)

ax.set_ylim(157, 163)
ax.set_yticks([157, 158, 159, 160, 161, 162, 163])
ax.tick_params(axis="y", direction="in")
ax.tick_params(axis="y", which="minor", direction="in")

ax.set_ylabel(r"CONDENSER EXIT"
              "\nTEMPERATURE, $^\circ$F", rotation='horizontal', ha='right',
              multialignment='center'
              )
ax.yaxis.set_label_coords(0.1, 1.1)

ax.set_xlim(0, 5)
ax.set_xticks([0, 1, 2, 3, 4, 5])
ax.set_xticklabels(["120:45", "120:47", "120:49", "120:51", "120:53", "120:55"])
ax.tick_params(axis="x", direction="in")
ax.tick_params(axis="x", which="minor", direction="in")

ax.set_xlabel(r"GROUND ELAPSED TIME, HR:MIN")

y = [
    161, 161, 159.5, 159.1, 159.1, 159.7, 161,
    161.05, 161.15, 161.15, 161.2, 161.2, 161.15, 161,
    161, 161, 159.2, 159.1, 159.1, 159.3, 159.7, 161,
    161.05, 161.15, 161.15, 161.2, 161.22, 161.21, 161.2, 161.18, 161.16, 161.12
]
x = np.array([
    0, 0.3, 0.35, 0.38, 0.4, 0.42, 0.44,
    0.46, 0.48, 0.5, 0.54, 0.6, 0.7, 1,
    3.25, 3.55, 3.63, 3.65, 3.67, 3.7, 3.72, 3.74,
    3.75, 3.78, 3.79, 3.81, 3.9, 3.98, 4, 4.1, 4.2, 4.5
])

plt.plot(x, y, "black")

title = "Figure 1-6. - Disturbance of Apollo 10 " \
        "\nfuel-cell temperature as it was identified in " \
        "\nin the laboratory."

ax.set_title(title, y=-0.2, pad=-40)

fig.tight_layout(**{"pad": 2})

plt.show()
