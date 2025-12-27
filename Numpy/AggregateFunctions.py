import numpy as np 

#   Aggregate functions = summarize date and typically return a single value .

array1 = np.array([
                    [1,2,3,4],
                    [5,6,7,8],
                    [9,10,11,12]
                    ])
print(np.sum(array1))
print(np.mean(array1))
print(np.std(array1))   # standard deviation
print(np.var(array1))   # variance
print(np.min(array1))  
print(np.max(array1))  
print(np.argmin(array1))  # position of minimum value
print(np.argmax(array1))  # position of maximum value

print(np.sum(array1,axis=0))   # coloumns sum
print(np.sum(array1,axis=1))   # rows sum

