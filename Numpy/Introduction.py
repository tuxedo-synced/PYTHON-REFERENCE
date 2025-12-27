import numpy as np 

# print version of np :
print(np.__version__)

# my_list = [1,2,3,4]
# my_list = my_list * 2
# print(my_list)  # [1, 2, 3, 4, 1, 2, 3, 4]

array = np.array([1,2,3,4])
print(type(array))  # <class 'numpy.ndarray'> n dimensional array .

array0 = np.array('A')
array1 = np.array([1,2,3,4,5])
array2 = np.array([
                    [1,2,3,4],
                    [4,5,6,7]
                  ])
array3 = np.array([
                    [
                    [1,2,3,4],
                    [4,5,6,7]
                    ],
                    [
                    [8,9,10,11],
                    [12,13,14,15]
                    ]
                  ])
print(f"{array0.ndim} dimensional array")
print(f"{array1.ndim} dimensional array")
print(f"{array2.ndim} dimensional array")
print(f"{array3.ndim} dimensional array")

print(array0.shape) 
print(array1.shape) 
print(array2.shape) 
print(array3.shape) 
# for 0 dimensional array: ()
# for 1 dimensional array: (coloumns)
# for 2 dimensional array: (rows,coloumns)
# for 3 dimensional array: (number_of_matrices,rows,coloumns)

print(array3[1][1][3])  # similar to C also called multi-dimensional indexing .
print(array3[1,1,3])




