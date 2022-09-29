#!/usr/bin/python3
"""Return information about an Employees TODO list"""

import requests
from sys import argv


if len(argv) < 2:
    quit()

if __name__ == '__main__':
    id = argv[1]
    user = requests.get(
        'https://jsonplaceholder.typicode.com/users', params={'id': id}
    ).json()[0]['name']
    todo = requests.get(
        'https://jsonplaceholder.typicode.com/todos', params={'userId': id}
    ).json()
    total = len(todo)

    # counting completed tasks
    completed = 0
    for task in todo:
        if task['completed'] is True:
            completed += 1

    # printing output
    print(f"Employee {user} is done with tasks({completed}/{total}):")

    # printing completed tasks
    [print(f"\t {task['title']}") for task in todo if task['completed'] is True]
