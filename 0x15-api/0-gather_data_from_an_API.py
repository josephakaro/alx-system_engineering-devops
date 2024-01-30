#!/usr/bin/python3
# Python script to print do to lists
import requests
import sys

def get_employee_todo_progress(employee_id):
    # Fetch user data
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response_user = requests.get(user_url)
    user_data = response_user.json()
    
    # Fetch user's TODO list
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    response_todos = requests.get(todos_url)
    todos_data = response_todos.json()

    # Calculate progress
    total_tasks = len(todos_data)
    completed_tasks = sum(task['completed'] for task in todos_data)
    
    # Display progress
    print(f"Employee {user_data['name']} is done with tasks ({completed_tasks}/{total_tasks}):")
    
    for task in todos_data:
        if task['completed']:
            print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)

