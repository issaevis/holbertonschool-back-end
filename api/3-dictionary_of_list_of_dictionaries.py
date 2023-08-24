#!/usr/bin/python3
'''using API to get data and export to JSON'''

import json
import requests

if __name__ == "__main__":
    todo_api = requests.get("https://jsonplaceholder.typicode.com/todos")
    user_api = requests.get("https://jsonplaceholder.typicode.com/users")

    todos_json = todo_api.text
    users_json = user_api.text

    todos = json.loads(todos_json)
    users = json.loads(users_json)

    user_tasks = {}

    for user in users:
        user_id = str(user["id"])
        user_tasks[user_id] = []

        for todo in todos:
            if todo["userId"] == user["id"]:
                user_tasks[user_id].append({
                    "username": user["username"],
                    "task": todo["title"],
                    "completed": todo["completed"]
                })
    filename = "todo_all_employees.json"
    with open(filename, "w") as f:
        json.dump(user_tasks, f, indent=2)
