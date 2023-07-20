import json
from pprint import pprint

# converting a python list to json
# json.dumps() method can convert a Python object into a JSON string.
# json.dump() method can be used for writing to JSON file.

students = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 27},
    {"name": "David", "age": 21},
    {"name": "Eve", "age": 20},
    {"name": "Fred", "age": 23},
    {"name": "Ginny", "age": 20},
    {"name": "Harriet", "age": 25},
    {"name": "Ileana", "age": 31},
    {"name": "Joseph", "age": 19},
    {"name": "Kincaid", "age": 21},
    {"name": "Larry", "age": 21},
    {"name": "Larr3y", "age": 24},
]

students = json.dumps(students, indent=2, sort_keys=True)
print(students)
