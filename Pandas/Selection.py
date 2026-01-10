import pandas as pd 

# df = pd.read_csv("Pandas/Pokemon.csv")
df = pd.read_csv("Pandas/Pokemon.csv" , index_col = "name") # by this a coloumn get access to serve as index 
# print(df.to_string())

# selection by coloumn/s
# print(df["name"].to_string())
# print(df["height"].to_string())
# print(df[["name" , "height" , "weight"]].to_string())

# selection by row/s
# print(df.loc["Venusaur"])
print(df.loc["Venusaur":"Weedle":2, ["height","weight"]].to_string)
# print(df.iloc[0:11:2 , 0:4:2])    # iloc[rowselection , coloumn selection]


# Excercise 
"""
pokemon = input("Enter the pokemons name: ")
try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} is not registered .")
"""



