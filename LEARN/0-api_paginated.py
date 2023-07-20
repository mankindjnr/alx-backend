"""
this method of using paginated API'S is not the best way to do it, but it is the easiest.
YOU need to know the limit of the API, and the offset. to use this method.
"""

import requests
from pprint import pprint

url = "https://pokeapi.co/api/v2/pokemon?limit=100"
response = requests.get(url)
data = response.json()

"""
offset - the starting point of the result set - number of records to skip
limit - the number of records to return
printing all the results from the api query above
"""
#pprint(data)

"""
how many results did we get from the api query above?
checking the output, we see there is a list of dictionaries.
we find the length of that list
"""
print(f"num of results: {len(data['results'])}")

"""
the result we get above, is the first page of results. as evident from the 
data output we get, the count is 1281, but we have gotten just 100 back. due to the
limit we set in the url. to get the next page of results, we need to use the next url

this gets the next url from the data output, if we want to get the next one hundred
results, we need to use this url
"""
next_url = data["next"]
url_page_2 = next_url
response_2 = requests.get(url_page_2)
data_2 = response_2.json()
pprint(data_2)

"""
we can also get the previous page of results, if we want to go back
"""
previous_url = data_2["previous"]
url_page_1 = previous_url
response_1 = requests.get(url_page_1)
data_1 = response_1.json()
#pprint(data_1)

"""
the next url from the 2nd page of results, is the 3rd page of results
"""
next_url_2 = data_2["next"]
url_page_3 = next_url_2
response_3 = requests.get(url_page_3)
data_3 = response_3.json()
#pprint(data_3)
 