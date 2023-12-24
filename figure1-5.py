import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

from font_settings import load_iso_font

load_iso_font()

fig = plt.figure(figsize=(5, 4.5), dpi=80)
ax = fig.add_subplot(111)

ax.spines[['right', 'top']].set_visible(False)

ax.set_ylim(140, 160)
ax.set_yticks([140, 150, 160, 170, 180])
ax.tick_params(axis="y", direction="in")
ax.tick_params(axis="y", which="minor", direction="in")

ax.set_ylabel(r"CONDENSER EXIT"
              "\nTEMPERATURE, $^\circ$F", rotation='horizontal', ha='right',
              multialignment='center'
              )
ax.yaxis.set_label_coords(0.1, 1.1)

plt.ylim(140, 180)
plt.xlim(0, 5.1)

ax.set_xticks([0, 1, 2, 3, 4, 5])
ax.set_xticklabels(["127:30", "128:00", "128:30", "129:00", "129:30", "130:00"])
ax.tick_params(axis="x", direction="in")
ax.tick_params(axis="x", which="minor", direction="in")

ax.set_label(r"GROUND ELAPSED TIME, HR:MIN")

y_extremes = [161.25, 157.5, 163, 153.75, 167, 150, 167, 150, 167, 150, 167, 150,
              167, 150, 167, 150, 164, 153.5, 162]

y_part_a = [160]
for y_val in y_extremes:
    y_part_a.append(y_val)
    y_part_a.append(y_val)
    y_part_a.append(y_val)
    y_part_a.append(160)

y_extremes = [161.5, 155, 163.75, 153, 167, 150, 167, 150, 167, 150, 167, 150, 167, 150, 167, 150, 167, 150,
              167, 150, 167, 150, 167, 150, 167, 152.5, 165, 156.25, 162.5]

y_part_b = [160]
for y_val in y_extremes:
    y_part_b.append(y_val)
    y_part_b.append(y_val)
    y_part_b.append(y_val)
    y_part_b.append(160)

x_part_a = np.linspace(0.2, 1, num=len(y_part_a))
spline = make_interp_spline(x_part_a, y_part_a, k=3)
x_part_a_new = np.linspace(0.2, 1, num=10 * len(y_part_a))
y_part_a_smooth = spline(x_part_a_new)

x_part_b = np.linspace(3.625, 5, num=len(y_part_b))
spline = make_interp_spline(x_part_b, y_part_b, k=3)
x_part_b_new = np.linspace(3.625, 5, num=10 * len(y_part_b))
y_part_b_smooth = spline(x_part_b_new)

y = np.concatenate([[160], y_part_a_smooth, y_part_b_smooth, [160]])
x = np.concatenate([[0], x_part_a_new, x_part_b_new, [5.1]])

plt.plot(x, y, "black")

title = "Figure 1-5. - Apollo 10 fuel-cell temperature" \
        "\noscillations as they originally appeared" \
        "\nin flight."

ax.set_title(title, y=-0.2, pad=-40)

fig.tight_layout(**{"pad": 2})

plt.show()
