#!/usr/bin/python3
"""Export information about an Employees TODO list to a csv file"""

import requests
from sys import argv


if len(argv) < 2:
    quit()

id = argv[1]
user = requests.get(
    'https://jsonplaceholder.typicode.com/users', params={'id': id}
).json()[0]['username']
todo = requests.get(
    'https://jsonplaceholder.typicode.com/todos', params={'userId': id}
).json()
total = len(todo)


with open('USER_ID.csv', "w") as file:
    for task in todo:
        print(
            f'"{id}","{user}","{task["completed"]}","{task["title"]}"',
            file=file)
