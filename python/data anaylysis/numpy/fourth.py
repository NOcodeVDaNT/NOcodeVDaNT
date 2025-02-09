import numpy as np

# Sorting
a = np.array([[20, 35], [50, 30]])

print("Row-wise sort:")
print(np.sort(a))  # Sort row-wise (default: axis=1)

print("Column-wise sort:")
print(np.sort(a, axis=0))  # Sort column-wise

print("Sort all elements into a 1D array:")
print(np.sort(a, axis=None))  # Sort all elements as a 1D array

print("-" * 80)

# Searching
print("Indices where a == 20:")
print(np.where(a == 50))  # Returns index of elements equal to 20

print("Indices where a > 20:")
print(np.where(a > 20))  # Returns indices where elements are greater than 20

# Convert to a sorted 1D array for np.searchsorted()
sorted_a = np.sort(a, axis=None)

print("Index where 20 should be inserted in sorted array:")
print(np.searchsorted(sorted_a, 20))  # Works only on sorted 1D array

print("Index where 20 should be inserted (right side):")
print(np.searchsorted(sorted_a, 20, side='right'))  # 'right' insertion

print("-" * 80)

# Filtering
print("Elements greater than 20:")
print(a[a > 20])  # Filters elements greater than 20

print("Elements less than 20:")
print(a[a < 20])  # Filters elements less than 20

print("Elements equal to 20:")
print(a[a == 20])  # Filters elements equal to 20



