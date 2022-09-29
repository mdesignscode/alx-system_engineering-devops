#!/usr/bin/python3
"""Export information about an Employees TODO list to a json file"""

from json import dump
from requests import get
from sys import argv


if len(argv) < 2:
    quit()

id = argv[1]
user = get(
    'https://jsonplaceholder.typicode.com/users', params={'id': id}
).json()[0]['name']
todo = get(
    'https://jsonplaceholder.typicode.com/todos', params={'userId': id}
).json()
total = len(todo)

status_list = []
for task in todo:
    status = {"task": task['title'], "completed": task["completed"], "username": user}
    status_list.append(status)

info = {f"{id}": status_list}

with open('USER_ID.json', "w") as file:
    dump(info, file)
