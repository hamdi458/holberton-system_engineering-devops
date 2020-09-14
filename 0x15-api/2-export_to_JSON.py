#!/usr/bin/python3
""" script to export data in the JSON format."""
from sys import argv
import json
import requests
if __name__ == "__main__":
    id = int(argv[1])
    r = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".
        format(id)).json()
    r_tasks_t_f = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".
        format(id)).json()
    tasks = []
    json_file = {}
    json_file[id] = tasks
    f = open('{}.json'.format(id), 'w')
    with f:
        for obj in r_tasks_t_f:
            f_json = {}
            f_json['task'] = obj['title']
            f_json['completed'] = obj.get('completed')
            f_json['username'] = r.get('username')
            tasks.append(f_json)
        json.dump(json_file, f)
