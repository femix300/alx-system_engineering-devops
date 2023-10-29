#!/usr/bin/python3
"""Saves information about employees' todo list in JSON format"""
import json
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    baseurl = 'https://jsonplaceholder.typicode.com/users/'
    url = baseurl + employee_id
    todourl = baseurl + employee_id + '/todos'
    r = requests.get(url)
    todos = requests.get(todourl).json()
    data = r.json()

    username = data['username']

    result = {employee_id: []}

    for item in todos:
        task = {
            "task": item['title'],
            "completed": item['completed'],
            "username": username,
        }
        result[employee_id].append(task)

    filename = f'{employee_id}.json'

    with open(filename, 'w') as json_file:
        json.dump(result, json_file)
