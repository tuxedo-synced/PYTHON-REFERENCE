import numpy as np 

# Scalar arthmetic

array1 = np.array([1,2,3])

print(array1+1)
print(array1-1)
print(array1*2) 
print(array1/2) 
print(array1 ** 5)

# Vectorized math funcs

array2 = np.array([1.5,1.6,1.7])
print(np.sqrt(array2))
print(np.round(array2))
print(np.floor(array2))
print(np.ceil(array2))
print(np.pi)

# Element-wise arthimetic 

array3 = np.array([1,2,3])
array4 = np.array([4,5,6])

print(array3 + array4)
print(array3 - array4)
print(array3 * array4)
print(array3 / array4)
print(array3 ** array4)

# Comparision operators

scores = np.array([91,23,45,88,100])

print(scores >= 35)

scores[scores < 60] = 0
print(scores)

