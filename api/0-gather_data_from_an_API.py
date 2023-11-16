#!/usr/bin/python3
"""For a given emp ID, returns info about his/her TODO list progress."""

import json
import urllib.request
from sys import argv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    user_id = argv[1]

    with urllib.request.urlopen(
        f'{url}/users/{user_id}/todos?_expand=user'
            ) as response:
        if response.getcode() == 200:
            jsondata = json.loads(response.read())
            name = jsondata[0]['user']['name']
            donetasks = [task for task in jsondata if task['completed']]
            numberdone = len(donetasks)
            alltasks = len(jsondata)

            first_str = f"Employer {name} is done with tasks"

            print(f"{first_str} ({numberdone}/{alltasks}):")
            for task in donetasks:
                print(f"\t {task['title']}")
        else:
            print(f"Error: {response.getcode()}")
