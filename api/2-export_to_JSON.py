#!/usr/bin/python3
"""Script to export data in the CSV / json format."""
import csv
import json
from sys import argv
import urllib.request

API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    USER_ID = argv[1]

    # User information
    user_url = f"{API_URL}/users/{USER_ID}"
    with urllib.request.urlopen(user_url) as user_response:
        if user_response.getcode() == 200:
            user_data = json.loads(user_response.read().decode('utf-8'))
        else:
            print(f"Error: {user_response.getcode()}")
            exit()

    # Todo list for the given user
    todo_url = f"{API_URL}/todos?userId={USER_ID}"
    with urllib.request.urlopen(todo_url) as todo_response:
        if todo_response.getcode() == 200:
            todo_data = json.loads(todo_response.read().decode('utf-8'))
        else:
            print(f"Error: {todo_response.getcode()}")
            exit()

    # Prepare data for export
    data = {
        USER_ID: [
            {
                "task": task['title'],
                "completed": task['completed'],
                "username": user_data['username']
            }
            for task in todo_data
        ]
    }

    # Write to JSON file
    with open(f"{USER_ID}.json", mode='w') as json_file:
        json.dump(data, json_file)

    # Write to CSV file
    with open(f"{USER_ID}.csv", mode='w', newline='') as csv_file:
        fieldnames = ["task", "completed", "username"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for task in data[USER_ID]:
            writer.writerow(task)

    print(f"Data has been exported to {USER_ID}.json and {USER_ID}.csv")
