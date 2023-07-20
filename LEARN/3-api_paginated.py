"""
waiting till the code breaks
"""
import requests
from pprint import pprint


url = "https://pokeapi.co/api/v2/pokemon?limit=100"

pokemon = []
offset = 0
limit = 100

while True:
    print("=======================")
    url = f"https://pokeapi.co/api/v2/pokemon?offset={offset}&limit={limit}"
    response = requests.get(url)
    data = response.json()

    try:
        pprint(data["results"][0])
    except:
        break
    
    pokemon.extend(data["results"])
    offset += 100
    print(url)
    #pprint(data)

print(len(pokemon))