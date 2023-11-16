#!/usr/bin/python3
"""returns info todo list progress based on the userid."""
import csv
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

            # Create and open a CSV file for writing
            csv_file_name = f"{target_user_id}.csv"
            with open(csv_file_name, mode='w', newline='') as csv_file:
                # Create a CSV writer for the CSV file
                csv_writer = csv.writer(csv_file)

                # Write the header for the CSV - not needed come to find out
                #csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

                # Write all tasks to the CSV file
                for task in todo_data:
                    # Convert the completed status to "True" or "False" not sort by completed
                    completed_status = "True" if task['completed'] else "False"
                    csv_writer.writerow([target_user_id, employee_name,
                                        completed_status, task['title']])

            print(f"CSV file '{csv_file_name}' has been created.")
        else:
            print(f"Error: {response.getcode()}")
