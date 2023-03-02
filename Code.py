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

