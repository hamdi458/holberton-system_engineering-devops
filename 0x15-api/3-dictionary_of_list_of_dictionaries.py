#!/usr/bin/python3
"""export data in the JSON format.
"""
import json
import requests
if __name__ == "__main__":
    r = requests.get(
        "https://jsonplaceholder.typicode.com/users").json()
    file_json = {}
    for obj in r:
        id = obj.get('id')
        r_user = requests.get(
            "https://jsonplaceholder.typicode.com/todos?userId={}".
            format(id)).json()
        r_tasks_t_f = requests.get(
            "https://jsonplaceholder.typicode.com/todos?userId={}".
            format(id)).json()
        tasks = []
        file_json[id] = tasks
        for obj1 in r_tasks_t_f:
            f_json = {}
            f_json["task"] = obj1.get('title')
            f_json["completed"] = obj1.get('completed')
            f_json["username"] = obj.get('username')
            tasks.append(f_json)
    f = open('todo_all_employees.json', 'w')
    with f:
        json.dump(file_json, f)
