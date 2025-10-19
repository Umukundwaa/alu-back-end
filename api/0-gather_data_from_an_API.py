#!/usr/bin/python3
"""
Script that fetches and displays an employee's TODO list progress
from JSONPlaceholder API
"""
import requests
import sys



def get_employee_todo_progress(employee_id):
    """
    Fetches employee TODO list progress and displays it

    Args:
        employee_id (int): The ID of the employee
    """
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee data
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch todos for the employee
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Calculate progress
    total_tasks = len(todos)
    completed_tasks = [todo for todo in todos if todo.get('completed')]
    number_of_done_tasks = len(completed_tasks)

    # Display results
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_tasks))

    # Display completed task titles
    for task in todos:
        if task.get('completed'):
            print("\t {}".format(task.get('title')))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)