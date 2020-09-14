#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import requests
from sys import argv
if __name__ == "__main__":
    id = int(argv[1])
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(id)).json()
    response_tasks = requests.get(
        "https://jsonplaceholder.typicode.com/todos?completed=true").json()

    s = 0
    for obj in response_tasks:
        if obj.get('userId') == id:
            s = s + 1
    response_tasks_t_f = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(id)).json()
    print("Employee {} is done with tasks({}/{}):".format(response.get("name"),
                                                          s, len(response_tasks_t_f)))
    for obj in response_tasks:
        if obj.get('userId') == id:
            print(obj.get("title"))
