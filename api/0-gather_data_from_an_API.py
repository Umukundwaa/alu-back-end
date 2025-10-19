#!/usr/bin/python3
"""
Script that uses a REST API for a given employee ID
to return information about their TODO list progress.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Fetch user and todos
    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    ).json()
    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    ).json()

    # Extract name and tasks
    employee_name = user.get("name")
    done_tasks = [t for t in todos if t.get("completed") is True]
    total_tasks = len(todos)
    done_count = len(done_tasks)

    # Print exactly as required
    print(
        f"Employee {employee_name} is done with tasks"
        f"({done_count}/{total_tasks}):"
    )

    for task in done_tasks:
        print(f"\t {task.get('title')}")