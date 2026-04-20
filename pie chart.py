# Data
import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]

# Create a pie chart
explode = [0, 0.1, 0, 0]
colors = ['gold', 'green', 'blue', 'yellow']
plt.pie(sizes, labels=labels,colors=colors, autopct='%1.1f%%')

# Add a title
plt.title('Basic Pie Chart')

# Show the plot
plt.show()
