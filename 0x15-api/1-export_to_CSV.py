#!/usr/bin/python3

"""script to export data in the CSV format"""

import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]
    user = requests.get("{}/users/{}".format(url, user_id)).json()
    todos = requests.get("{}/todos?userId={}".format(url, user_id)).json()
    with open("{}.csv".format(user_id), "w") as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [
            csvwriter.writerow(
                [
                    user_id,
                    user.get("username"),
                    task.get("completed"),
                    task.get("title"),
                ]
            )
            for task in todos
        ]
