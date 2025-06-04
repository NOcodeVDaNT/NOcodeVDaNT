#barchart
import matplotlib.pyplot as plt
def plot_barchart(x, y):
    plt.bar(x, y, color='skyblue', edgecolor='black')
    
    plt.xlabel('X-axis name')
    plt.ylabel('Y-axis name')
    plt.title('Sample Bar Chart')
    plt.xticks(rotation=45)
    
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
    
x = ["m", "t", "w", "th", "fri"]
y = [2, 3, 5, 7, 11]
plot_barchart(x, y)
