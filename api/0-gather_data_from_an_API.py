#!/usr/bin/python3
'''using API to get data'''


import sys
import requests
import json


if __name__ == "__main__":
    todo_api = requests.get("https://jsonplaceholder.typicode.com/todos")
    user_api = requests.get("https://jsonplaceholder.typicode.com/users")

    todos_json = todo_api.text
    users_json = user_api.text

    todos = json.loads(todos_json)
    users = json.loads(users_json)

    for select_user in users:
        if int(select_user["id"]) == int(sys.argv[1]):
            user = select_user

    done_tasks = []
    done_tasks_counter = 0
    all_count = 0

    for todo in todos:
        if todo["userId"] == user["id"]:
            if todo["completed"] is True:
                done_tasks.append(todo["title"])
                done_tasks_counter += 1
            all_count += 1

    print("Employee {} is done with tasks ({}/{})".format
          (user["name"], done_tasks_counter, all_count))
    for task in done_tasks:
        print("\t {}".format(task))
