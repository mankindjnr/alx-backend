"""
the second method is LISTENING TO THE API
since all the queries have a next url, we can use that to get the next page of results
till there is no next url. this is the best way to do it, but it is a bit more complicated

we start with passing the first url we have to a variable
"""
import requests
from pprint import pprint

#our initatial url
next_url = "https://pokeapi.co/api/v2/pokemon?limit=100"
pokemon = []
#we use a while loop to keep getting the next url, till there is no next url
while next_url:
    print("=======================")
    response = requests.get(next_url)
    data = response.json()

    pokemon.extend(data["results"])

    #updatingt the url
    next_url = data["next"]
    print(next_url)
    #pprint(data)

print(f"num of results: {len(pokemon)}")
