import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)
ax.plot([1, 2, 3], [2, 4, 6], "r--")
ax.plot([1, 2, 3], [3, 2, 1], "g-")
ax.set_title("Example plot")
plt.show()

# 1. Does this code create one plotting panel (Axes object) or two?
# Explain briefly. A panel is a plotting area, not an individual x-axis or y-axis.
# Your answer: just one plotting panel, because the code says plt.subplots(1,1) which creates a figure with 1 row and 1 column of plotting areas.

# 2. How many data lines are drawn? What are the y-values of the red dashed line?
# Your answer: 2 datalines. y-values of red dashed line are 2, 4 and 6
