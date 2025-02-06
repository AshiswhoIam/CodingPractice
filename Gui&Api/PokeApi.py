#Learning to connect Api using python

import requests

base_url="https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url=f"{base_url}/pokemon/{name}"
    response= requests.get(url)
    #200 success.
    print(response)

    if response.status_code == 200: 
        #convert to python dictionary
        pokemon_data=response.json()
        return pokemon_data
        #print(pokemon_data)
        #print("Response is, fine data retrieved")
    else:
        print(f"failed to retrieve the data {response.status_code}")
pokemon_name = "Dragonite"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info["name"].capitalize()}")
    print(f"ID: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}")
    print(f"Weight: {pokemon_info["weight"]}")