#piehart
import matplotlib.pyplot as plt
def plot_piechart(labels, sizes):
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['gold', 'lightcoral', 'lightskyblue'])
    
    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is a circle.
    plt.title('Sample Pie Chart')
    plt.show()
    
labels = ['Category A', 'Category B', 'Category C']
sizes = [15, 30, 45]
plot_piechart(labels, sizes)
