#scatterplot
import matplotlib.pyplot as plt
def plot_scatter(x, y):
    plt.scatter(x, y, color='blue', marker='o', s=100, alpha=0.7)
    
    plt.xlabel('X-axis name')
    plt.ylabel('Y-axis name')
    plt.title('Sample Scatter Plot')
    plt.grid(True)
    
    plt.show()
    
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plot_scatter(x, y)
