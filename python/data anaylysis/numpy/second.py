import numpy as np

a=np.array([1,2,3,4,5]) 
b=np.array([5,6,7,8,9])

print(a.ndim)
print(b.ndim)


print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)


           
           
#operation of two matrix
print("-----------------------------------------------------------------------------------")
c=np.array([[1,2,3],[4,5,6],[7,8,9]])
d=np.array([[11,21,31],[41,51,61],[71,81,91]])
print(c+d)
print(c-d)
print(c*d)
print(c/d)

print("-----------------------------------------------------------------------------------")

#concatenate

print(np.concatenate((c,d))) #by deafult axis=0
print(np.concatenate((c,d),axis=1))

print("-----------------------------------------------------------------------------------")




