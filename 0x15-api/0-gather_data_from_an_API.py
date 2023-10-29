#!/usr/bin/python3
"""Returns information about an employees to do list"""
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

    employeename = data['name']
    done_tasks = 0
    tasks = 0

    for item in todos:
        if item['completed']:
            done_tasks += 1
        tasks += 1

    print(f"Employee {employeename} is done with tasks({done_tasks}/{tasks}):")
    for title in todos:
        if title['completed']:
            print(f"\t {title['title']}")
