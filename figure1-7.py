import matplotlib.patches as patches
import matplotlib.pyplot as plt

from font_settings import load_iso_font

load_iso_font()

fig = plt.figure(figsize=(10, 6), dpi=100)
ax = fig.add_subplot(111)

ax.spines[['left', 'top', "right"]].set_visible(False)

width = 80
height = 16

text = {
    "APOLLO 5": "LM\nDEVELOPMENT",
    "APOLLO 7": "MANNED\nCSM\nOPERATIONS",
    "APOLLO 8": "CSM OPERATIONS,\nLUNAR DISTANCE",
    "APOLLO 9": "COMBINED CSM-\nLM OPERATIONS\nEARTH ORBIT",
    "APOLLO 10": "COMBINED\nOPERATIONS\nLUNAR DISTANCE",
    "APOLLO 11": "LANDING SURFACE\nOPERATIONS\nASCENT",
}

labels = ["Apollo 4 AND 6"]
labels.extend([x for x in text.keys()])

ax.xaxis.set_tick_params(length=0)
ax.set_xticks([(x * width)+width/2 for x in range(7)], labels)
ax.set_yticks([])

r1 = patches.Rectangle((0, 0), width, height, edgecolor="black", facecolor="white", zorder=10)
ax.add_patch(r1)
ax.text((width/2), 5, "SPACECRAFT\nREENTRY", ha="center", zorder=100)
ax.text((width/2), height+5, "SATURN V\nDEVELOPMENT", ha="center", zorder=100)

r1 = patches.Rectangle((0, height), width, height, edgecolor="black", facecolor="white", zorder=10)
ax.add_patch(r1)

num_of_boxes = 2
for x, text in zip(range(width, 7 * width, width), text.values()):
    num = 0
    for box_num in range(num_of_boxes):
        r1 = patches.Rectangle((x, box_num * height), width, height,
                               edgecolor="black", facecolor="white", hatch="////", linewidth=0.5)
        ax.add_patch(r1)
        num = box_num

    num += 1
    r1 = patches.Rectangle((x, num * height), width, height, edgecolor="black", facecolor="white", linewidth=1, zorder=10, clip_on=False)
    ax.add_patch(r1)

    if text.count("\n") == 1:
        offset = 5
    else:
        offset = 3
    ax.text(x + (width/2), (num*height)+ offset, text, ha="center", zorder=100)

    num_of_boxes += 1

ax.set_xlim(0, 7 * width)
ax.set_ylim(0, 8 * height)

title = "Figure 1-7. - Buildup of Apollo mission capability."
ax.set_title(title, y=-0.12)
plt.show()
