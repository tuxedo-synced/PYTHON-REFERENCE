import pandas as pd 

data = {
    "Name": ["Itachi","Tobi","Kabuto"],
    "Age": [18,14,34],
}

# df = pd.DataFrame(data) # default index
df = pd.DataFrame(data , index = ["Employee 1" , "Employee 2" , "Employee 3"])
print(df,end = "\n\n")

# selct a single row
print(df.loc["Employee 1"], end = "\n\n")

# can also use integer location to select a single row 
print(df.iloc[0],end = "\n\n")

# add a new coloumn 
df["Job"] = ["berozgaar" , "Doctor" , "Scientist"]

print(df,end = "\n\n")

# add a new row
new_row = pd.DataFrame([{"Name": "Tsunade" , "Age": 106 , "Job": "Hokage"},
                        {"Name": "Hinata" , "Age": 53 , "Job": "Hokage Wife"},
                        ], index = ["Employee 4","Employee 5"])
df = pd.concat([df , new_row])
print(df)



