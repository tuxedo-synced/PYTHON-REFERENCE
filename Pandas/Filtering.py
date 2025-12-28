import pandas as pd 

df = pd.read_csv("Pandas/Pokemon.csv" , index_col = "name")

# Filtering = keeping the rows that match a condition 

# tall_pokemon = df[df["height"] >= 2]
# print(tall_pokemon)

# legendary_pokemon = df[df["legendary"]]
# print(legendary_pokemon)

# water_pokemon = df[(df["type1"] == "Water") | (df["type2"] == "Water")]
# print(water_pokemon)

