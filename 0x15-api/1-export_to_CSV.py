#!/usr/bin/python3
"""returns information about an employee TODO list progress."""
import csv
import json
import requests
from sys import argv


def get_todos(u_id):
    """export to csv format"""
    url = 'https://jsonplaceholder.typicode.com/'
    evruser = json.loads(requests.get('{}users/{}'.format(url, u_id)).text)
    data = requests.get('{}users/{}/todos'.format(url, u_id))
    content = json.loads(data.text)

    keys = ['id', 'name', 'completed', 'title']
    with open('{}.csv'.format(u_id), 'wt') as file:
        for value in content:
            value['id'] = u_id
            value['name'] = evruser['username']
        dict_writer = csv.DictWriter(file,
                                     keys,
                                     extrasaction='ignore',
                                     quoting=csv.QUOTE_ALL,
                                     lineterminator='\n')
        dict_writer.writerows(content)


if __name__ == '__main__':
    if len(argv) >= 2:
        get_todos(argv[1])
