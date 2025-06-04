
import matplotlib.pyplot as plt
def plot_data(x, y):
    plt.plot(x, y, marker='o', linestyle='--', color='red', markersize=8, linewidth=2)
    plt.fill_between(x, y, color='pink', alpha=0.9)
    
    
    
    plt.xlabel('X-axis name')
    plt.ylabel('Y-axis name')
    plt.title('Sample Plot')
    plt.legend(['sales'])
    plt.xticks(rotation=45)
    
    plt.grid(True)
    plt.show()

x = ["m", "t", "w", "th", "fri"]
y = [2, 3, 5, 7, 11]
plot_data(x, y)
    



