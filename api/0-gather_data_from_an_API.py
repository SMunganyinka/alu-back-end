#!/usr/bin/python3
"""
Script that retrieves and displays an employee's TODO list progress
using a REST API.
"""

import json
import requests
import sys

if __name__ == "__main__":
    session = requests.Session()
    emp_id = sys.argv[1]
    tasks_url = f'https://jsonplaceholder.typicode.com/users/{emp_id}/todos'
    user_url = f'https://jsonplaceholder.typicode.com/users/{emp_id}'
    tasks_response = session.get(tasks_url)
    user_response = session.get(user_url)
    tasks = tasks_response.json()
    emp_name = user_response.json().get('name')
    completed_tasks = [task for task in tasks if task['completed']]
    print(f"Employee {emp_name} is done with tasks"
          f"({len(completed_tasks)}/{len(tasks)}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")
