"""
continuing till there are no more results
useful when you are not provided with the next url
"""
import requests


url = "https://pokeapi.co/api/v2/pokemon?limit=100"
pokemon = []

offset = 0
limit = 100

while True:
    print("=======================")
    url = f"https://pokeapi.co/api/v2/pokemon?offset={offset}&limit={limit}"
    response = requests.get(url)
    data = response.json()

    if not data["results"]:
        break

    pokemon.extend(data["results"])
    offset += 100
    print(url)
    #pprint(data)

print(len(pokemon))