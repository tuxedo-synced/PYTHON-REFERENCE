import pandas as pd 

# aggregate functions = Reduces a set of values into a single summary value
#                       used to smmarize and analyze data
#                       often used with the groupby() function .

df = pd.read_csv(r"Pandas\Pokemon.csv", index_col = "name")

# print(df.mean(numeric_only = True))
# print(df.sum(numeric_only = True))
# print(df.min(numeric_only = True))
# print(df.max(numeric_only = True))
# print(df.count())

# single coloumn 

print(df["height","weight"].mean())
# print(df["height"].sum())
# print(df["height"].min())
# print(df["height"].max())
# print(df["height"].count())

group = df.groupby("type1")
# print(group["height"].mean())
# print(group["height"].sum())
# print(group["height"].min())
# print(group["height"].max())
