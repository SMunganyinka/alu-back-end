#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress and exports data in JSON format.
"""

import json
import requests

if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    todo_all = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        task_list = [{"username": username, "task": task.get("title"),
                      "completed": task.get("completed")} for task in todos
                     if task.get("userId") == user_id]
        todo_all[user_id] = task_list
    with open("todo_all_employees.json", "w") as f:
        json.dump(todo_all, f, indent=4)
