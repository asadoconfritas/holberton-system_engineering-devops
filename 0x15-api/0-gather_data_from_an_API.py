#!/usr/bin/python3
"""returns information about an employee TODO list progress."""
import json
import requests
from sys import argv


if __name__ == "__main__":
    todos = 'https://jsonplaceholder.typicode.com/todos?userId={}'\
            .format(int(argv[1]))
    allusers = 'https://jsonplaceholder.typicode.com/users/{}'\
            .format(int(argv[1]))
    counter = 0
    tasks = 0
    ret = requests.get(todos).json()
    user = requests.get(allusers).json()
    for elem in ret:
        if elem.get('completed') is True:
            counter += 1
        tasks += 1
    print('Employee {} is done with tasks({}/{}):'
            .format(user.get('name'), done, tasks))
    for elem in ret:
        if elem.get('completed') is True:
            print('\t {}'.format(elem.get('title')))
