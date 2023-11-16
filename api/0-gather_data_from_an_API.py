#!/usr/bin/python3
"""returns info todo list progress based on the userid."""
import json
from sys import argv
import urllib.request


if __name__ == '__main__':
    # Base URL for the JSONPlaceholder API
    base_api_url = 'https://jsonplaceholder.typicode.com'

    # Retrieve user ID from command-line arguments
    target_user_id = argv[1]

    # Make a request to the API to fetch the to-do list for the specified user
    with urllib.request.urlopen(
        f'{base_api_url}/users/{target_user_id}/todos?_expand=user'
    ) as response:
        if response.getcode() == 200:
            # Load JSON data from the response
            todo_data = json.loads(response.read())

            # Extract employee name from the first task
            employee_name = todo_data[0]['user']['name']

            # Filter completed tasks
            completed_tasks = [task for task in todo_data if task['completed']]
            num_completed_tasks = len(completed_tasks)
            total_tasks = len(todo_data)

            # Display the summary
            first_line = (
                f"Employee {employee_name} is done with tasks"
                f"({num_completed_tasks}/{total_tasks}):")
            print(first_line)

            for task in completed_tasks:
                print(f"\t {task['title']}")
        else:
            print(f"Error: {response.getcode()}")
