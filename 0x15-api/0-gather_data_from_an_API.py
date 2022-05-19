#!/usr/bin/python3
"""returns information about an employee TODO list progress."""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """program ind"""
    url = 'https://jsonplaceholder.typicode.com/users/'
    r = requests.get("{}/{}".format(url, argv[1]))
    name = r.json().get('name')

    req = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                       .format(argv[1]))
    todos = json.loads(req.text)
    tasks = len(todos)
    # print(tasks)
    count = 0
    incompl = 0
    task_ist = []
    for task in todos:
        if task.get('completed') is True:
            count += 1
            task_ist.append(task)
        else:
            incompl += 1
    print("Employee {} is done with tasks({}/{}):".
          format(name, count, tasks))

    for task in task_ist:
        print("\t", task.get('title'))
