import numpy as np

a=np.array([1,2,3,4,5])
print(a)
print("-----------------------------------------------------------------------------------")
#matrix 
b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b)
print("-----------------------------------------------------------------------------------")

#slice

print(a[0:3])
print(a[3:])
print(a[:3])

print("-----------------------------------------------------------------------------------")

print(b[0:2,0:3]) # row 0 to 2 and column 0 to 3
print(b[1:,1:])
print(b[:2,:2])

print("-----------------------------------------------------------------------------------")

#shape
print(a.shape)
print(b.shape)

#3d array
c=np.array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]])
print(c.shape)

print("-----------------------------------------------------------------------------------")

#reshape
print(a.reshape(5,1))

#length
print(len(a))
print(len(b))
print(len(c))

print("-----------------------------------------------------------------------------------")

#size
print(a.size)
print(b.size)
print(c.size)

print("-----------------------------------------------------------------------------------")

#datatype
print(a.dtype)
print(b.dtype)
print(c.dtype)

print("-----------------------------------------------------------------------------------")

#zeros
print(np.zeros((3,3)))

#ones
print(np.ones((3,3)))

#identity matrix
print(np.eye(3))

print("-----------------------------------------------------------------------------------")

#random
print(np.random.rand(3,3))

#convert type
print(a.astype(float))

print("-----------------------------------------------------------------------------------")

#no of rows and columns
print(b.shape)
print("no of rows:"+str(b.shape[0])+" no of columns:"+str(b.shape[1]))






