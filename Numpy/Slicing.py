import numpy as np 

array1 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
# variable_name[start:end:step]     [start,end)   ->  sllicer operator
print(array1[0:4:2])
# coloum selection :- variable_name[rows_part,coloumns_part]
print(array1[:,0])
print(array1[:,0:4:2])
print(array1[:,::-1])
print(array1[0,::-1])

