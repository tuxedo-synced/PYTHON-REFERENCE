import pandas as pd 

# Data Cleaning = the process of fixing/removing:
#                 incomplete, incorrect, or irrelavent data.
#                 ~75% of work done with Pandas is data cleaning 

df = pd.read_csv(r"Pandas\Pokemon.csv")

# 1. Drop irrelavent coloumns
# df = df.drop(columns=["legendary","no"])
# print(df.to_string())

# 2. Handle missing data 

# df = df.dropna(subset=["type2"])    # the rows are removed with NaN values .
# print(df.to_string())

# df = df.fillna({"type2": "None"})   # this helps in filling NaN values with some other preffered name .
# print(df.to_string())

# 3. Fix inconsistent values
# df["type1"] = df["type1"].replace({"Grass": "GRASS",
#                                     "Fire": "FIRE",
#                                     "Water": "WATER"
#                                     })
# print(df.to_string())

# 4. Standardize text
# df["name"] = df["name"].str.lower()
# print(df.to_string())

# 5. Fix data types
# df["legendary"] = df["legendary"].astype(bool)
# print(df.to_string())

# 6. remove duplicate entries 
# firstly add duplicates while practicing .
# print(df.to_string())
# df = df.drop_duplicates()
# print(df.to_string())
