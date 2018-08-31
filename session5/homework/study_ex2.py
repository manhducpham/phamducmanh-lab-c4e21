from matplotlib import pyplot

# 1. prepare data
machine_counts = [11, 3, 1]
# 2. prepare labels
machine_labels = ['PC', 'MAC', 'Linux']
# 3. draw pie
pyplot.pie(machine_counts, labels = machine_labels, autopct = "%.1f%%", shadow = True, explode = [0, 0.2, 0])
pyplot.title('PC vs. MAC vs. Linux users')
pyplot.axis('equal')
# 4 .show
pyplot.show()