import matplotlib.pyplot as plt

def plot_histogram(data, bins):
    plt.hist(data, bins=bins, color='skyblue', edgecolor='black', alpha=0.7)
    
    plt.xlabel('Marks')
    plt.ylabel('Number of Students')
    plt.title('Distribution of Student Marks')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(bins)  # Align ticks to bin edges
    plt.show()

marks = [88, 73, 45, 67, 90, 56, 32, 77, 84, 69,
         91, 53, 38, 60, 72, 95, 81, 49, 66, 59]

custom_bins = [30, 44, 58, 72, 86, 100]

plot_histogram(marks, custom_bins)
