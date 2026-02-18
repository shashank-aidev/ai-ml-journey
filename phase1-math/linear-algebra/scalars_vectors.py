import numpy as np
v=np.array([1,2,3]) #[1,2,3] this is normal python list but ""np.array()"" using this convert it into array
print(v)

#now add 2 arrays
v1 = np.array([1, 2, 3])
print(type(v))
v2 = np.array([4, -1, 2]) 
#it will add the values presnt in the same index like [0] of v1 + [0] of v2 will give 5

print(v1 + v2)

#multiplication
v=np.array([1,2,3])
print(v*3)

print(np.zeros(2)) # np.zeros will create an array having zero at each index and (2) is how many element we won't in the aray
#Used to initialize weights in ML.

print("Shape of v:", v.shape)
print("Number of dimensions:", v.ndim)
'''
Shape of v: (3,) #this means it hase 3 element and 1 dimension the cumma matters (3,) it is tuple
Number of dimensions: 1
'''

#new logic 
v1 = np.array([1,2,3])
v2 = np.array([[1,2,3]])

print("v1 shape:", v1.shape)
print("v2 shape:", v2.shape) #it means 2D array and 1 row and 3 columns This is a matrix
print("v2 ndim:", v2.ndim)

#new example
# Column vector
v3 = np.array([[1,0],
               [2,0],
               [3,0]])

print("v3 shape:", v3.shape)
print("v3 ndim:", v3.ndim)



