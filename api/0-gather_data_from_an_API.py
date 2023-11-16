#!/usr/bin/python3
"""returns info todo list progress based on the userid."""
import json
import urllib.request
from sys import argv

if __name__ == '__main__':
    base_api_url = 'https://jsonplaceholder.typicode.com'
    target_user_id = argv[1]

    with urllib.request.urlopen(
        f'{base_api_url}/users/{target_user_id}/todos?_expand=user'
    ) as response:
        if response.getcode() == 200:
            todo_data = json.loads(response.read())
            employee_name = todo_data[0]['user']['name']

            completed_tasks = [task for task in todo_data if task['completed']]
            num_completed_tasks = len(completed_tasks)
            total_tasks = len(todo_data)

            first_str = f"Employee {employee_name} is done with tasks"

            print(f"{first_str} ({num_completed_tasks}/{total_tasks}):")
            for task in completed_tasks:
                print(f"\t {task['title']}")
        else:
            print(f"Error: {response.getcode()}")
