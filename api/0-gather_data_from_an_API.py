#!/usr/bin/env python3
"""
Python script that fetches employee TODO list progress from a REST API.
For a given employee ID, returns information about their TODO list progress.
"""

import sys
import requests
import json


def fetch_employee_data(employee_id):
    """
    Fetch employee information and TODO tasks from the API.
    
    Args:
        employee_id (int): The ID of the employee
        
    Returns:
        tuple: (employee_info, todos) or (None, None) if error occurs
    """
    base_url = "https://jsonplaceholder.typicode.com"
    
    try:
        # Fetch employee information
        user_response = requests.get(f"{base_url}/users/{employee_id}")
        user_response.raise_for_status()
        
        if user_response.status_code == 404:
            print(f"Error: Employee with ID {employee_id} not found")
            return None, None
            
        employee_info = user_response.json()
        
        # Fetch TODO tasks for the employee
        todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
        todos_response.raise_for_status()
        todos = todos_response.json()
        
        return employee_info, todos
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None, None
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON response: {e}")
        return None, None


def display_todo_progress(employee_info, todos):
    """
    Display the employee TODO list progress in the specified format.
    
    Args:
        employee_info (dict): Employee information from the API
        todos (list): List of TODO items for the employee
    """
    employee_name = employee_info.get('name', 'Unknown')
    
    # Count completed and total tasks
    completed_tasks = [todo for todo in todos if todo.get('completed', False)]
    total_tasks = len(todos)
    completed_count = len(completed_tasks)
    
    # Display the first line with employee name and task progress
    print(f"Employee {employee_name} is done with tasks({completed_count}/{total_tasks}):")
    
    # Display completed task titles with proper indentation (1 tab + 1 space)
    for task in completed_tasks:
        task_title = task.get('title', 'No title')
        print(f"\t {task_title}")


def main():
    """
    Main function to handle command-line arguments and orchestrate the script.
    """
    # Check if employee ID argument is provided
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    # Validate and parse employee ID
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)
    
    # Fetch employee data from API
    employee_info, todos = fetch_employee_data(employee_id)
    
    if employee_info is None or todos is None:
        sys.exit(1)
    
    # Display the TODO progress
    display_todo_progress(employee_info, todos)


if __name__ == "__main__":
    main()

