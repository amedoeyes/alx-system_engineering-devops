#!/usr/bin/python3

"""
script that, using this REST API, for a given employee ID, returns information
about his/her TODO list progress
"""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]
    user = requests.get("{}/users/{}".format(url, user_id)).json()
    todos = requests.get("{}/todos?userId={}".format(url, user_id)).json()
    completed = [task for task in todos if task.get("completed") is True]
    print(
        "Employee {} is done with tasks({}/{}):".format(
            user.get("name"), len(completed), len(todos)
        )
    )
    [print("\t {}".format(task.get("title"))) for task in completed]
