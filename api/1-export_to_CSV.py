#!/usr/bin/python3
"""
Script that retrieves and displays an employee's TODO list progress
using a REST API and exports data to a CSV file.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    session = requests.Session()
    emp_id = sys.argv[1]
    tasks_url = (
        f'https://jsonplaceholder.typicode.com/users/{emp_id}/todos'
    )
    user_url = (
        f'https://jsonplaceholder.typicode.com/users/{emp_id}'
    )
    tasks_response = session.get(tasks_url)
    user_response = session.get(user_url)
    tasks = tasks_response.json()
    emp_data = user_response.json()
    emp_name = emp_data.get('name')
    username = emp_data.get('username')
    completed_tasks = [task for task in tasks if task['completed']]
    print(
        f"Employee {emp_name} is done with tasks({len(completed_tasks)}/"
        f"{len(tasks)}):"
    )
    for task in completed_tasks:
        print(f"\t {task['title']}")
        file_name = f"{emp_id}.csv"
    with open(file_name, "w", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([
                emp_id, username, task['completed'], task['title']
            ])
