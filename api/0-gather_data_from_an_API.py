#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com"

    # Get user information
    user_url = "{}/users/{}".format(base_url, employee_id)
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Employee not found.")
        sys.exit(1)

    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Get TODO list for user
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Filter completed tasks
    completed_tasks = [task for task in todos if task.get("completed") is True]

    # Print required output
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), len(todos)
    ))

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))

