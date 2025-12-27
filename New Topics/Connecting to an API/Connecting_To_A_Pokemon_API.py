# how to connect to an API using python
import  requests 

base_url = r"https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    resoponse = requests.get(url)
    print(resoponse)    # <Response [200]> --> it means ok

    if resoponse.status_code == 200:
        pokemon_data = resoponse.json()
        return pokemon_data
    else:
        print(f"Failed to retrive data {resoponse.status_code}")

if __name__ == "__main__":
    pokemon_name = input("Enter pokemon name: ")
    info_of_specific = get_pokemon_info(pokemon_name)
    if info_of_specific:
        print(f"pokemon name -> {info_of_specific["name"]}")
        print(f"{pokemon_name}'s id -> {info_of_specific["id"]}")
        print(f"{pokemon_name}'s height-> {info_of_specific["height"]}")
        print(f"{pokemon_name}'s weight -> {info_of_specific["weight"]}")