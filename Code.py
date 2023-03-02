import matplotlib.pyplot as plt
import numpy as np
categories = ["A", "B","C","D","E", "F"]
player1_stats = [70,50,45,60,80,60]

N= len (categories)
angles=[n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111,polar=True)
stats = player1_stats + player1_stats [:1]

ax.plot(angles, stats, linewidth=2,linestyle="solid", label="Player 1")
ax.fill(angles, stats, alpha=0.4)
ax.set_thetagrids(np.degrees(angles[:-1]), categories)
ax.set_ylim(0,100)
plt.title("Spider Chart")
plt.legend(loc="upper right", bbox_to_anchor=(1.3,1.1))
plt.show()


#Or

import matplotlib.pyplot as plt
import pandas as pd
from math import pi

# Set data
df = pd.DataFrame({
    'group': ['A', 'B', 'C', 'D'],
    'A': [30, 20, 10, 40],
    'B': [30, 20, 10, 40],
    'C': [30, 20, 10, 40],
    'D': [30, 20, 10, 40],
    'E': [30, 20, 10, 40]
})

# ------- PART 1: Create background

# number of variable
categories = list(df)[1:]
N = len(categories)

# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

# Initialise the spider plot
ax = plt.subplot(111, polar=True)

# If you want the first axis to be on top:
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)

# Draw one axe per variable + add labels
plt.xticks(angles[:-1], categories)

# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([10, 20, 30], ["10", "20", "30"], color="grey", size=7)
plt.ylim(0, 40)

# ------- PART 2: Add plots

# Plot each individual = each line of the data
# I don't make a loop, because plotting more than 3 groups makes the chart unreadable

# Ind1
values = df.loc[0].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="Group A")
ax.fill(angles, values, 'b', alpha=0.1)

# Ind2
values = df.loc[1].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="Group B")
ax.fill(angles, values, 'r', alpha=0.1)

# Ind3
values = df.loc[2].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="Group C")
ax.fill(angles, values, 'r', alpha=0.1)

# Ind4
values = df.loc[3].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="Group D")
ax.fill(angles, values, 'r', alpha=0.1)

# Add legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

# Show the graph
plt.show()

