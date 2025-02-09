import numpy as np
#add and remove element

a=np.array([[20,40],[60,80]])
a=np.append(a,[[100,200]],axis=0) #np.append give a new array do not modified the original array
print(a)

#insert element

a=np.insert(a,1,[[10,30]],axis=0) #insert at index 1
print(a)

#indexing
print(a[0])  #o/p=[20 40]
print(a[0][0]) #o/p=20

#delete element
a=np.delete(a,1,axis=0)
print(a)


