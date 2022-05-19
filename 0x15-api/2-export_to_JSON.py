#!/usr/bin/python3
"""returns information about an employee TODO list progress."""
import csv
import json
import requests
from sys import argv


def get_todos2(u_id):
    """export to json format"""
    url = 'https://jsonplaceholder.typicode.com/'
    evruser = json.loads(requests.get('{}users/{}'.format(url, u_id)).text)
    data = requests.get('{}users/{}/todos'.format(url, u_id))
    content = json.loads(data.text)

    keys = ['id', 'name', 'completed', 'title']
    with open('{}.json'.format(u_id), 'wt') as file:
        dictionary = []
        aux = {}
        aux[u_id] = []
        for value in content:
            task_dict = {}
            task_dict['task'] = value['title']
            task_dict['completed'] = value['completed']
            task_dict['username'] = evruser['username']
            aux[u_id].append(task_dict)
        json.dump(aux, file)
        dict_writer = csv.DictWriter(file,


if __name__ == '__main__':
    if len(argv) >= 2:
        get_todos2(argv[1])
