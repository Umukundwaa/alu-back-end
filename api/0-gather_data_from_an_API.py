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

    # URLs
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    # Corrected: fetch the user by ID to get exact name
    user_data_url = f"https://jsonplaceholder.typicode.com/users/{employee_Id}"

    # Get user data
    user_response = requests.get(user_data_url)
    employee_name = user_response.json().get("name")

    # Get all todos
    todo_response = requests.get(todo_url)
    todos = todo_response.json()

    # Filter completed tasks for this employee
    done = []
    total = 0
    completed = 0
    for todo in todos:
        if todo.get("userId") == employee_Id:
            total += 1
            if todo.get("completed"):
                completed += 1
                done.append(todo.get("title"))

    # Display the progress information
    print(f"Employee {employee_name} is done with tasks({completed}/{total}):")
    for task_title in done:
        print(f"\t {task_title}")
