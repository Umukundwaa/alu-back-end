#!/usr/bin/python3
"""
Getting data using API
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_Id = int(sys.argv[1])

    # Get employee data
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_Id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200 or not user_response.json():
        print("Employee not found")
        sys.exit(1)
    employee_name = user_response.json().get("name")

    # Get employee's todos
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_Id}/todos"
    todo_response = requests.get(todo_url)
    todos = todo_response.json()

    total = len(todos)
    done_tasks = [t.get("title") for t in todos if t.get("completed")]

    # Print progress
    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total}):")
    for task_title in done_tasks:
        print(f"\t {task_title}")
