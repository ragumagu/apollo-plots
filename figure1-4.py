import matplotlib.pyplot as plt

from font_settings import load_iso_font

load_iso_font()

fig = plt.figure(figsize=(4.5, 4), dpi=80)
ax = fig.add_subplot(111)

ax.spines[['right', 'top']].set_visible(False)

ax.set_ylim(0, 12)
ax.set_xlim(0.5, 3)

ax.tick_params(axis="x", direction="in")
ax.tick_params(axis="y", direction="in")
ax.tick_params(axis="x", which="minor", direction="in")
ax.tick_params(axis="y", which="minor", direction="in")

percentages = [3.5, 6.8, 10.3]
labels = ["DESIGN", "WORKMANSHIP", "TOTAL"]

bar = ax.bar([1, 2, 3], percentages, width=0.25, label=labels, hatch=["xxxx", "", "\\\\\\\\"], color="white",
             edgecolor='black', clip_on=False)
ax.bar_label(bar, padding=3, fmt=lambda x: f"{x}%")

ax.set_yticks([0, 2, 4, 6, 8, 10, 12])

ax.set_ylabel(r"PERCENT"
              "\n"
              r"FAILURE", rotation='horizontal', ha='right',
              multialignment='center'
              )

ax.set_xticks([])
ax.legend(loc=(0.05, 0.75), frameon=False)

title = "Figure 1-4. - Results of thermal " \
        "\nacceptance tests for 3685 tests of " \
        "\n127 different components."
plt.title(title, y=-0.4)

fig.tight_layout(**{"pad": 2})

plt.show()
