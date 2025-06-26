#!/usr/bin/python3
"""
Script that retrieves and displays an employee's TODO list progress
using a REST API and exports the data in JSON format.
"""
import json
import requests
import sys

if __name__ == "__main__":
    session = requests.Session()
    emp_id = sys.argv[1]
    tasks_url = (f'https://jsonplaceholder.typicode.com/users/{emp_id}/todos')
    user_url = (f'https://jsonplaceholder.typicode.com/users/{emp_id}')
    tasks_response = session.get(tasks_url)
    user_response = session.get(user_url)
    tasks = tasks_response.json()
    user_data = user_response.json()
    emp_name = user_data.get('name')
    username = user_data.get('username')
    completed_tasks = [task for task in tasks if task['completed']]
    print(f"Employee {emp_name} is done with tasks ({len(completed_tasks)}/"
          f"{len(tasks)}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")
    tasks_list = [{"task": task["title"], "completed": task["completed"],
                   "username": username} for task in tasks]
    json_data = {emp_id: tasks_list}
    file_name = f"{emp_id}.json"
    with open(file_name, "w") as json_file:
        json.dump(json_data, json_file, indent=4)
    print(f"Data exported to {file_name}")
