#!/usr/bin/python3

"""
Gather data from APIs and save them into a CSV file format
"""


import csv
import requests
from requests.exceptions import RequestException
import sys


def user_employee(user_Id):
    try:
        user_url = "https://jsonplaceholder.typicode.com/users"
        user_request = requests.get(user_url + "/" + user_Id)
        user_request.raise_for_status()
        user_response = user_request.json()
    except RequestException as e:
        print(f"User can not be found,\n{e}")

    employee_name = user_response.get('username')
    employee_id = int(user_Id)

    employee_todos(employee_name, employee_id)


def employee_todos(Emp_name, Emp_id):
    try:
        todos_url = "https://jsonplaceholder.typicode.com/todos"
        todos_request = requests.get(todos_url)
        todos_request.raise_for_status()
        todos_response = todos_request.json()
    except RequestException as e:
        print(f"Todos not found,\n{e}")

    todos_data = []
    for count in todos_response:
        if count.get('userId') == Emp_id:
            todos_data.append(count)

    csv_formatting(Emp_name, todos_data, Emp_id)


def csv_formatting(Emp_name, todos_data, Emp_id):
    filename = Emp_id
    with open('{}.csv'.format(filename), 'w', newline='') as user_file:
        # fieldnames = ['USER_ID', 'USERNAME',
        #               'TASK_COMPLETED_STATUS', 'TASK_TITLE']

        # thewriter = csv.DictWriter(user_file, fieldnames=fieldnames)

        # thewriter.writeheader()

        for tasks in todos_data:
            user_file.write('"{}","{}","{}","{}"\n'.format(
                filename,
                Emp_name,
                tasks.get('completed'),
                tasks.get('title')
            ))
        # for tasks in todos_data:
        #     thewriter.writerow({
        #         'USER_ID': "{}".format(tasks.get('userId')),
        #         'USERNAME': "{}".format(Emp_name),
        #         'TASK_COMPLETED_STATUS': "{}".format(tasks.get('completed')),
        #         'TASK_TITLE': "{}".format(tasks.get('title'))
        #     })

        # if thewriter:
        #     print(f"{user_file.name} was created successfuly!!")


def main():
    Emp_ID = sys.argv[1]
    user_employee(Emp_ID)


if __name__ == "__main__":
    main()
