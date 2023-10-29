#!/usr/bin/python3
"""Saves information about employees todo list in csv format"""
import csv
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

    filename = "USER_ID.csv"

    with open(filename, mode='w', newline='') as file:
        for item in todos:
            file.write('"{}","{}","{}","{}"\n'.format(
                username,
                item['userId'],
                item['completed'],
                item['title'],
            ))
