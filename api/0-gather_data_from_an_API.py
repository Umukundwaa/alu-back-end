#!/usr/bin/python3
"""
getting data using api
"""
import requests
import sys

if __name__ == "__main__":
    employee_Id = int(sys.argv[1])

    todo_url = "https://jsonplaceholder.typicode.com/todos"
    # ✅ FIX STARTS HERE — use the endpoint with employee ID
    user_data_url = f"https://jsonplaceholder.typicode.com/users/{employee_Id}"
    user_response = requests.get(user_data_url)
    employee_name = user_response.json().get("name")
    # ✅ FIX ENDS HERE

    todo_response = requests.get(todo_url)
    todos = todo_response.json()

    # filter completed tasks
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
    for _ in done:
        print(f"\t {_}")
