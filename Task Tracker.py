import json
import os
from datetime import datetime
import argparse

TASK_FILE = "/content/tasks.json"

# Initialize storage
def init_storage():
    if not os.path.exists(TASK_FILE):
        with open(TASK_FILE, "w") as f:
            json.dump([], f)

# Load tasks
def load_tasks():
    with open(TASK_FILE, "r") as f:
        return json.load(f)

# Save tasks
def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Add task
def add_task(description):
    tasks = load_tasks()
    new_id = 1 if not tasks else max(task["id"] for task in tasks) + 1
    now = datetime.now().isoformat()
    task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task added (ID: {new_id})")

# List tasks
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found.")
        return
    for task in tasks:
        print(f"[{task['id']}] {task['description']} - {task['status']}")

# Update task
def update_task(task_id, new_desc):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_desc
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(✏️ Task updated.")
            return
    print("❌ Task not found.")

# Delete task
def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t['id'] != task_id]
    if len(new_tasks) == len(tasks):
        print("❌ Task not found.")
    else:
        save_tasks(new_tasks)
        print("🗑️ Task deleted.")

# Mark task
def mark_task(task_id, status):
    if status not in ["done", "todo"]:
        print("❌ Status must be 'done' or 'todo'")
        return
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"🔄 Task marked as {status}.")
            return
    print("❌ Task not found.")

# Command handling
def main():
    init_storage()
    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="Command to run", choices=["add", "list", "update", "delete", "mark"])
    parser.add_argument("--id", type=int, help="Task ID (for update/delete/mark)")
    parser.add_argument("--desc", type=str, help="Task description (for add/update)")
    parser.add_argument("--status", type=str, help="Task status: done or todo (for mark)")
    args = parser.parse_args()

    try:
        if args.command == "add":
            if not args.desc:
                raise ValueError("Description is required to add a task.")
            add_task(args.desc)

        elif args.command == "list":
            list_tasks()

        elif args.command == "update":
            if args.id is None or not args.desc:
                raise ValueError("Both --id and --desc are required for update.")
            update_task(args.id, args.desc)

        elif args.command == "delete":
            if args.id is None:
                raise ValueError("--id is required to delete.")
            delete_task(args.id)

        elif args.command == "mark":
            if args.id is None or not args.status:
                raise ValueError("Both --id and --status are required for marking.")
            mark_task(args.id, args.status)

    except Exception as e:
        print("❌ Error:", e)

# Simulate input in Google Colab
def run_cli(command_line):
    import sys
    sys.argv = ["task_tracker"] + command_line.strip().split()
    main()