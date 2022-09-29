#!/usr/bin/python3
"""Export information about an Employees TODO list to a json file"""

from json import dump
from requests import get

# { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}

info_dict = {}
for id in range(1,11):
    user = get(
        'https://jsonplaceholder.typicode.com/users', params={'id': id}
    ).json()[0]['name']
    todo = get(
        'https://jsonplaceholder.typicode.com/todos', params={'userId': id}
    ).json()
    total = len(todo)

    status_list = []
    for task in todo:
        status = {"task": task['title'],
                  "completed": task["completed"], "username": user}
        status_list.append(status)

    info = {f"{id}": status_list}
    info_dict[f'{id}'] = info

with open('todo_all_employees.json', "w") as file:
    dump(info_dict, file)
