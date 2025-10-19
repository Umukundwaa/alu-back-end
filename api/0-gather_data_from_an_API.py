#!/usr/bin/python3
"""
Script that uses a REST API for a given employee ID
to return information about their TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    # Make sure an employee ID is provided
    if len(sys.argv) < 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    # Get employee ID from command line argument
    employee_id = int(sys.argv[1])

    # Define API endpoints
    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = f"{base_url}users/{employee_id}"
    todos_url = f"{base_url}todos?userId={employee_id}"

    # Fetch user and TODO data
    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    # Convert responses to JSON
    user_data = user_response.json()
    todos_data = todos_response.json()

    # Extract employee name
    employee_name = user_data.get("name")

    # Calculate completed and total tasks
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get("completed")]

    # Print required output
    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):")

    for task in done_tasks:
        print(f"\t {task.get('title')}")