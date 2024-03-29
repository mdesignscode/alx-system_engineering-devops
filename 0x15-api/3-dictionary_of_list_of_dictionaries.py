#!/usr/bin/python3
"""Export information about an Employees TODO list to a json file"""

from json import dump
from requests import get


if __name__ == '__main__':
    info_dict = {}
    for id in range(1, 11):
        user = get(
            'https://jsonplaceholder.typicode.com/users', params={'id': id}
        ).json()[0]['username']
        todo = get(
            'https://jsonplaceholder.typicode.com/todos', params={'userId': id}
        ).json()
        total = len(todo)

        status_list = []
        for task in todo:
            status = {"username": user, "task": task['title'],
                      "completed": task["completed"], }
            status_list.append(status)

        info_dict[f'{id}'] = status_list

    with open('todo_all_employees.json', "w") as file:
        dump(info_dict, file)
