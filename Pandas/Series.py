import pandas as pd 

# Series = A Pandas 1-Dimensional labeled array that can hold any data type 
#          Think of it like a single coloumn in a spreadsheet (1-DImensional)

data1 = [100, 102, 104]
data2 = [100.1, 102.2, 104.3]
data3 = ["A", "B", "C"]
data4 = [True , False , True]

series_1 = pd.Series(data1)    # cosntructor
series_2 = pd.Series(data2)    # cosntructor
series_3 = pd.Series(data3)    # cosntructor
series_4 = pd.Series(data4)    # cosntructor

print(series_1,end = "\n\n")
print(series_2,end = "\n\n")
print(series_3,end = "\n\n")
print(series_4,end = "\n\n")

# we can also set index to the constructor 

series_1 = pd.Series(data1 , index = ["first wala" , "second wala" , "third wala"])
print(series_1,end = "\n\n")

