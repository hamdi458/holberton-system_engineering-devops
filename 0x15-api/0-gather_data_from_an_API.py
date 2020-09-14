#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import requests
from sys import argv
if __name__ == "__main__":
    id = int(argv[1])
    r = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".
        format(id)).json()
    r_tasks = requests.get(
        "https://jsonplaceholder.typicode.com/todos?completed=true").json()

    s = 0
    for obj in r_tasks:
        if obj.get('userId') == id:
            s = s + 1
    r_tasks_t_f = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".
        format(id)).json()
    print("Employee {} is done with tasks({}/{}):".format(r.get("name"),
                                                          s,
                                                          len(r_tasks_t_f)))
    for obj in r_tasks:
        if obj.get('userId') == id:
            print("\t", obj.get("title"))
