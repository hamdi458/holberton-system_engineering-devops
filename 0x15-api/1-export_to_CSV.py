#!/usr/bin/python3
"""export data in the CSV format."""
import csv
import requests
from sys import argv
if __name__ == "__main__":
    id = int(argv[1])
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".
        format(id)).json()
    response_tasks_t_f = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".
        format(id)).json()
    f = open('{}.csv'.format(id), 'w')
    with f:
        line = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
        for obj in response_tasks_t_f:
            line.writerow([id, response.get('username'),
                          obj['completed'], obj.get('title')])
