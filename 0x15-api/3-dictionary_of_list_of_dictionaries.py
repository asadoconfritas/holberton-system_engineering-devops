#!/usr/bin/python3
"""returns information about an employee TODO list progress."""
import json
import csv
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    users = json.loads(requests.get('{}users/{}'.format(url, u_id)).text)

    keys = ['id', 'name', 'completed', 'title']
    aux = {}
    with open('todo_all_employees.json', 'wt') as file:
        for u in users:
            todo_list = requests.get('{}users/{}/todos'.format(url, u['id']))
            todo_list = json.loads(todo_list.text)
            aux[u['id']] = []
            for value in todo_list:
                task_dict = {}
                task_dict['task'] = value['title']
                task_dict['completed'] = value['completed']
                task_dict['username'] = u['username']
                aux[u['id']].append(task_dict)
            json.dump(aux, file)
