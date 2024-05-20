#!/usr/bin/python3

"""script to export data in the JSON format"""

import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]
    user = requests.get("{}/users/{}".format(url, user_id)).json()
    todos = requests.get("{}/todos?userId={}".format(url, user_id)).json()
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(
            {
                user_id: [
                    {
                        "task": task.get("title"),
                        "completed": task.get("completed"),
                        "username": user.get("username"),
                    }
                    for task in todos
                ]
            },
            jsonfile,
        )
