#!/usr/bin/python3
"""Script to export data in the JSON format."""
import csv
import json
from sys import argv
import urllib.request

API_URL = 'https://jsonplaceholder.typicode.com'

def fetch_user_data(user_id):
    user_url = f"{API_URL}/users/{user_id}"
    with urllib.request.urlopen(user_url) as user_response:
        if user_response.getcode() == 200:
            return json.loads(user_response.read().decode('utf-8'))
        else:
            print(f"Error fetching user data for ID {user_id}: {user_response.getcode()}")
            exit()

def fetch_todo_data(user_id):
    todo_url = f"{API_URL}/todos?userId={user_id}"
    with urllib.request.urlopen(todo_url) as todo_response:
        if todo_response.getcode() == 200:
            return json.loads(todo_response.read().decode('utf-8'))
        else:
            print(f"Error fetching todo data for ID {user_id}: {todo_response.getcode()}")
            exit()

if __name__ == '__main__':
    all_users_data = {}

    for user_id in argv[1:]:
        user_id = int(user_id)

        user_data = fetch_user_data(user_id)
        todo_data = fetch_todo_data(user_id)

        user_tasks = [{
                "username": user_data['username'],
                "task": task['title'],
                "completed": task['completed']}
            for task in todo_data]

        all_users_data[user_id] = user_tasks

    # Write to JSON file
    with open("todo_all_employees.json", mode='w') as json_file:
        json.dump(all_users_data, json_file)

    
    #print("Data has been exported to todo_all_employees.json")
