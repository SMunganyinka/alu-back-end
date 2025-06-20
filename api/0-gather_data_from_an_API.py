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

    # Fetch user info
    user_url = "{}/users/{}".format(base_url, employee_id)
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Employee not found.")
        sys.exit(1)

    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch todos
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Completed tasks
    done_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)
    done_count = len(done_tasks)

    # Output
    print("Employee {} is done with tasks({}/{}):".format(employee_name, done_count, total_tasks))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))


