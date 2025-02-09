import numpy as np

#aggregate function

a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)

print("sum of all element in array")
print(np.sum(a))

print("sum of all element in row")
print(np.sum(a,axis=1))

print("sum of all element in column")
print(np.sum(a,axis=0))

print("-----------------------------------------------------------------------------------")

print("mean of all element in array")
print(np.mean(a))

print("mean of all element in row")
print(np.mean(a,axis=1))

print("mean of all element in column")
print(np.mean(a,axis=0))

print("-----------------------------------------------------------------------------------")

print("median of all element in array")
print(np.median(a))

print("median of all element in row")
print(np.median(a,axis=1))

print("median of all element in column")
print(np.median(a,axis=0))

print("-----------------------------------------------------------------------------------")

print("standard deviation of all element in array")
print(np.std(a))

print("standard deviation of all element in row")
print(np.std(a,axis=1))

print("standard deviation of all element in column")
print(np.std(a,axis=0))

print("-----------------------------------------------------------------------------------")

print("variance of all element in array")
print(np.var(a))

print("variance of all element in row")
print(np.var(a,axis=1))

print("variance of all element in column")
print(np.var(a,axis=0))

print("-----------------------------------------------------------------------------------")

print("min of all element in array")
print(np.min(a))

print("min of all element in row")
print(np.min(a,axis=1))

print("min of all element in column")
print(np.min(a,axis=0))

print("-----------------------------------------------------------------------------------")

print("max of all element in array")
print(np.max(a))

print("max of all element in row")
print(np.max(a,axis=1))

print("max of all element in column")
print(np.max(a,axis=0))

print("-----------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------")


import numpy as np
scores = np.array([50, 60, 70, 80, 90, 100])  # Exam scores
print("50th Percentile (Median):", np.percentile(scores, 50))  # Median
print("25th and 75th Percentiles:", np.percentile(scores, [25, 75]))
print("90th Percentile:", np.percentile(scores, 90))

#The median (75) means half of the students scored below 75.
# The 25th percentile (62.5) means 25% of students scored below 62.5.
# The 75th percentile (87.5) means 75% of students scored below 87.5.
# The 90th percentile (95) means 90% of students scored below 95.

