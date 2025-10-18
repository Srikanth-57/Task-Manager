import sys

TASK_FILE = "tasks.txt"

def load_tasks():
    """Reads tasks from the file."""
    try:
        with open(TASK_FILE, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Writes tasks to the file."""
    with open(TASK_FILE, 'w') as f:
        for task in tasks:
            f.write(f"{task}\n")

def add_task(description):
    """Adds a new task."""
    tasks = load_tasks()
    tasks.append(description)
    save_tasks(tasks)
    print(f"✅ Added task: '{description}'")

def view_tasks():
    """Displays all current tasks."""
    tasks = load_tasks()

    print("\n--- PROJECT: TASK MANAGER ---")

    if not tasks:
        print("  List is empty! Time to add some tasks.")
        return

    for i, task in enumerate(tasks, 1):
        print(f"  {i}. {task}")
    print("--------------------------\n")
    


def main():
    if len(sys.argv) < 2:
        
        view_tasks()
        return

    command = sys.argv[1]

    if command == "add" and len(sys.argv) > 2:
        task_description = " ".join(sys.argv[2:])
        add_task(task_description)
    elif command == "view":
        view_tasks()
    elif command == "delete" and len(sys.argv) > 2:
        print("Delete command placeholder executed.")
    else:
        print("Usage:")
    
    if command == "add" and len(sys.argv) > 2:
        task_description = " ".join(sys.argv[2:])
        add_task(task_description)
    elif command == "view":
        view_tasks()
    else:
        print("Usage:")
        print("  python task_manager.py add [description of task]")
        print("  python task_manager.py view")
        print("\nNote: Only 'add' and 'view' commands are supported.")

if __name__ == "__main__":
    main()