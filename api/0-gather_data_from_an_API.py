#!/usr/bin/python3
"""TODO list progress for an employee ID."""
import json
import urllib.request
from sys import argv

if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: python script_name.py <user_id>")
        exit(1)

    url = 'https://jsonplaceholder.typicode.com'
    user_id = argv[1]

    try:
        with urllib.request.urlopen(
                f'{url}/users/{user_id}/todos?_expand=user'
        ) as response:
            if response.getcode() == 200:
                jsondata = json.loads(response.read())
                if jsondata:
                    name = jsondata[0]['user']['name']
                    donetasks = [task for task in jsondata if task['completed']]
                    numberdone = len(donetasks)
                    alltasks = len(jsondata)

                    first_str = f"Employee {name} is done with tasks"

                    print(f"{first_str} ({numberdone}/{alltasks}):")
                    for task in donetasks:
                        print(f"\t {task['title']}")
                else:
                    print(f"No data found for user ID {user_id}")
            else:
                print(f"Error: {response.getcode()}")
    except urllib.error.URLError as e:
        print(f"Error: {e}")
