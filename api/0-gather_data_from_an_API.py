#!/usr/bin/python3
"""
Script that uses a REST API for a given employee ID
to return information about their TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    # Check argument count
    if len(sys.argv) < 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user and todos
    user = requests.get(url + f"users/{employee_id}").json()
    todos = requests.get(url + f"todos?userId={employee_id}").json()

    # Extract the correct employee name
    employee_name = user.get("name")

    # Count completed tasks
    done_tasks = [t for t in todos if t.get("completed")]
    total_tasks = len(todos)
    done_count = len(done_tasks)

    # ✅ Exact format required
    print(f"Employee {employee_name} is done with tasks({done_count}/{total_tasks}):")

    for task in done_tasks:
        print(f"\t {task.get('title')}")
