import matplotlib.pyplot as plt

from font_settings import load_iso_font

load_iso_font()

fig = plt.figure(figsize=(5.5, 4), dpi=80)
ax = fig.add_subplot(111)
ax.spines[['right', 'top']].set_visible(False)

ax.set_xlim(0, 20)
ax.set_ylim(30, 130)
ax.tick_params(axis="x", direction="in")
ax.tick_params(axis="y", direction="in")
ax.tick_params(axis="x", which="minor", direction="in")
ax.tick_params(axis="y", which="minor", direction="in")

ax.plot([0, 1, 4, 5, 9, 10, 14.5, 15.5, 18, 19], [75, 75, 130, 130, 30, 30, 130, 130, 75, 75], color="black")

ax.set_yticks([30, 75, 130])
ax.set_xticks([0, 5, 10, 15, 20])

ax.yaxis.set_label_coords(0.1, 1)

ax.set_ylabel(r"TEMPERATURE,"
              "\n"
              r"$^\circ$F", rotation='horizontal', ha='right',
              multialignment='center'
              )
ax.set_xlabel("TIME, HR")

ax.axvline(4, ymin=1.05, ymax=1.15, color="black", clip_on=False, linewidth=1)
ax.axvline(5, ymin=1.05, ymax=1.15, color="black", clip_on=False, linewidth=1)
ax.annotate('', xy=(0.20, 1.1), xycoords='axes fraction', xytext=(0.15, 1.1), va='center',
            arrowprops=dict(arrowstyle="->", color='black', lw=0.5))
ax.annotate('1 HR (MINIMUM)', xy=(0.25, 1.1), xycoords='axes fraction', xytext=(0.31, 1.1), va='center',
            arrowprops=dict(arrowstyle="->", color='black', lw=0.5))

title = "Figure 1-2. - Thermal test level for acceptance"
plt.title(title, y=-0.4)

fig.tight_layout(**{"pad": 2})

plt.show()
