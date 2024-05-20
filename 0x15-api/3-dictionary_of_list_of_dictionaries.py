#!/usr/bin/python3

"""script to export data in the JSON format"""

import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get("{}/users".format(url)).json()
    all_data = {}
    for user in users:
        user_id = user.get("id")
        user_todos = requests.get(f"{url}/todos?userId={user_id}").json()
        all_data[user_id] = [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user.get("username"),
            }
            for task in user_todos
        ]
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_data, jsonfile)
