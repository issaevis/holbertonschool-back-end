#!/usr/bin/python3
'''using API to get data'''


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

    user = None

    for select_user in users:
        if int(select_user["id"]) == int(sys.argv[1]):
            user = select_user
            break

    if user is None:
        print("User not found")
        sys.exit(1)

    user_tasks = []

    for todo in todos:
        if todo["userId"] == user["id"]:
            user_tasks.append({
                "task": todo["title"],
                "completed": todo["completed"],
                "username": user["username"]
            })

    filename = "{}".format(user["id"]) + ".json"

    with open(filename, "w", newline="") as f:
        json.dump({str(user["id"]): user_tasks}, f, indent=2)
