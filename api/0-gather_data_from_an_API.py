#!/usr/bin/python3
"""Script that, using this REST API, for a given employee"""
import requests
from sys import argv

apiforurl = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    user_info_response = requests.get(f"{apiforurl}/users/{argv[1]}")
    user_data = user_info_response.json()

    tasks_response = requests.get(f"{apiforurl}/todos?userId={argv[1]}")
    task_info  tasks_response.json()

    completed_tasks = [task for task in task_info if task['completed']]

    emp_name = user_data["name"]
    num_completed_tasks = len(completed_tasks)
    all_tasks = len(task_info)

    print("Employee {} is done with tasks({}/{}):".format(
        emp_name, num_completed_tasks, all_tasks))

    for task in completed_tasks:
        print(f"\t {task['title']}")
