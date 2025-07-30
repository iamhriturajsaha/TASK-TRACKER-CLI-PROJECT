# 📝 Task Tracker CLI Project

A lightweight and intuitive Command-Line Interface (CLI) tool for managing your daily tasks. Built with Python, it stores tasks locally in JSON format—no database setup required.

## ✨ Features

- **Add Tasks** – Create new tasks with descriptions
- **List Tasks** – View all pending and completed tasks
- **Update Tasks** – Modify task descriptions
- **Delete Tasks** – Remove unwanted tasks
- **Mark Complete** – Toggle task status between pending and done
- **Local Storage** – All data stored in `tasks.json` (works offline)
- **Cross-Platform** – Compatible with Windows, macOS and Linux

## 🛠️ Requirements

- Python 3.6 or higher
- No external dependencies required

## 🚀 Quick Start

### Installation

1. **Clone the repository - **
   ```bash
   git clone https://github.com/iamhriturajsaha/TASK-TRACKER-CLI-PROJECT
   cd TASK-TRACKER-CLI-PROJECT
   ```

2. **Make it executable -**
   ```bash
   chmod +x Task Tracker.py
   ```

3. **Verify installation -**
   ```bash
   python Task Tracker.py --help
   ```

### Basic Usage

```bash
# Add a new task
python Task Tracker.py add "Buy groceries for the week"

# List all tasks
python Task Tracker.py list

# Mark task as complete
python Task Tracker.py done 1

# Update a task
python Task Tracker.py update 1 "Buy organic groceries"

# Delete a task
python Task Tracker.py delete 1
```

## 📋 Command Reference

### Add Tasks
```bash
python Task Tracker.py add "Task description"
python Task Tracker.py add "Learn Python CLI development"
```

### List Tasks
```bash
# List all tasks
python Task Tracker.py list

# List only pending tasks
python Task Tracker.py list --status pending

# List only completed tasks
python Task Tracker.py list --status done
```

### Update Tasks
```bash
python Task Tracker.py update <task_id> "New description"
python Task Tracker.py update 2 "Complete project documentation"
```

### Mark Tasks as Done
```bash
python Task Tracker.py done <task_id>
python Task Tracker.py done 1
```

### Delete Tasks
```bash
python Task Tracker.py delete <task_id>
python Task Tracker.py delete 3
```

## 📊 Example Session

```bash
$ python Task Tracker.py add "Review project proposal"
✅ Task added successfully (ID: 1)

$ python Task Tracker.py add "Schedule team meeting"
✅ Task added successfully (ID: 2)

$ python Task Tracker.py list
📋 Your Tasks:
1. [PENDING] Review project proposal
2. [PENDING] Schedule team meeting

$ python Task Tracker.py done 1
✅ Task 1 marked as done

$ python Task Tracker.py list
📋 Your Tasks:
1. [DONE] Review project proposal
2. [PENDING] Schedule team meeting
```

## 💾 Data Storage

Tasks are stored in `tasks.json` with the following structure -

```json
[
  {
    "id": 1,
    "description": "Buy groceries",
    "status": "pending",
    "created_at": "2025-01-15T10:30:00"
  },
  {
    "id": 2,
    "description": "Complete homework",
    "status": "done",
    "created_at": "2025-01-15T11:45:00"
  }
]
```

## 🔧 Advanced Usage

### Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv task-env

# Activate (Linux/macOS)
source task-env/bin/activate

# Activate (Windows)
task-env\Scripts\activate

# Install and use
python Task Tracker.py --help
```

### Alias for Quick Access
Add to your shell profile (`.bashrc`, `.zshrc`, etc.):
```bash
alias tasks="python /path/to/Task Tracker.py"
```

Then use -
```bash
tasks add "New task"
tasks list
```

## 🧹 Maintenance

### Reset All Tasks
```bash
# Remove the data file to start fresh
rm tasks.json        # Linux/macOS
del tasks.json       # Windows
```

### Backup Tasks
```bash
# Create a backup
cp tasks.json tasks_backup.json

# Restore from backup
cp tasks_backup.json tasks.json
```





