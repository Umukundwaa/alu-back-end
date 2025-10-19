#!/usr/bin/python3
"""
Fetch and display TODO list progress for a given employee ID.
"""
import requests
import sys

if __name__ == "__main__":
    # Check if employee ID is passed
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    emp_id = int(sys.argv[1])

    # API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}/todos"

    # Fetch user and todos data
    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    # Extract data
    emp_name = user.get("name")
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]

    # Display results
    print(f"Employee {emp_name} is done with tasks({len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")
