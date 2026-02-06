import numpy as np
myarray1 = np.arange(1,11) #np.array([1,2,3,4,5,6,7,8,9,10])
#print(myarray1)

myarray2 = np.arange(1,10).reshape(3,3)
#print(myarray2)

myList = [10,20,30,40,50]
myarray3 = np.array(myList)

print("Array 1 ---->  ")
print(myarray1)
print(myarray1.shape)
print(myarray1.dtype)

print("Array 2 ---->  ")
print(myarray2)
print(myarray2.shape)
print(myarray2.dtype)

print("Array 3 ---->  ")
print(myarray3)
print(myarray3.shape)
print(myarray3.dtype)