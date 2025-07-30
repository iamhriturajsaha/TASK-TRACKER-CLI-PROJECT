import json
import os
import argparse

# File to store tasks
TASK_FILE = "tasks.json"

# Load existing tasks or start fresh
def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as f:
        return json.load(f)

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Add a task
def add_task(description):
    tasks = load_tasks()
    task_id = max([t["id"] for t in tasks], default=0) + 1
    task = {"id": task_id, "description": description, "status": "pending"}
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task added with ID {task_id}")

# List all tasks
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📂 No tasks found.")
        return
    for task in tasks:
        print(f"{task['id']}. [{task['status'].upper()}] {task['description']}")

# Update task description
def update_task(task_id, new_desc):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_desc
            save_tasks(tasks)
            print(f"✏️ Task {task_id} updated.")
            return
    print("❌ Task not found.")

# Delete a task
def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]
    if len(new_tasks) == len(tasks):
        print("❌ Task not found.")
    else:
        save_tasks(new_tasks)
        print(f"🗑️ Task {task_id} deleted.")

# Mark task as completed
def mark_done(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            save_tasks(tasks)
            print(f"✅ Task {task_id} marked as done.")
            return
    print("❌ Task not found.")

# Setup CLI arguments
def main():
    parser = argparse.ArgumentParser(prog="task_tracker")
    subparsers = parser.add_subparsers(dest="command")

    # Add command
    add = subparsers.add_parser("add", help="Add a new task")
    add.add_argument("--desc", required=True, help="Task description")

    # List command
    subparsers.add_parser("list", help="List all tasks")

    # Update command
    update = subparsers.add_parser("update", help="Update a task's description")
    update.add_argument("--id", type=int, required=True, help="Task ID")
    update.add_argument("--desc", required=True, help="New description")

    # Delete command
    delete = subparsers.add_parser("delete", help="Delete a task")
    delete.add_argument("--id", type=int, required=True, help="Task ID")

    # Mark done command
    mark = subparsers.add_parser("mark", help="Mark a task as done")
    mark.add_argument("--id", type=int, required=True, help="Task ID")

    # Parse and execute
    args = parser.parse_args()

    if args.command == "add":
        add_task(args.desc)
    elif args.command == "list":
        list_tasks()
    elif args.command == "update":
        update_task(args.id, args.desc)
    elif args.command == "delete":
        delete_task(args.id)
    elif args.command == "mark":
        mark_done(args.id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()