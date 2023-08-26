#!/usr/bin/python3
'''using API to get data and export to CSV'''


import csv
import json
import requests
import sys


if __name__ == "__main__":
    todo_api = requests.get("https://jsonplaceholder.typicode.com/todos")
    user_api = requests.get("https://jsonplaceholder.typicode.com/users")

    todos_json = todo_api.text
    users_json = user_api.text

    todos = json.loads(todos_json)
    users = json.loads(users_json)

    tasks_id = []

    for select_user in users:
        if int(select_user["id"]) == int(sys.argv[1]):
            user = select_user
            break

    if user is None:
        print("User not found")
        sys.exit(1)

    filename = "{}".format(user["id"]) + ".csv"

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
        for todo in todos:
            if todo["userId"] == user["id"]:
                writer.writerow([str(user["id"]), user["username"],
                                str(todo["completed"]), todo["title"]])

    f.close()
