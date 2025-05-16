import json
import os

TASK_FILE = "tasks.json"

# Load tasks from file if exists
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []  # Return empty list if file is empty or invalid
    return []


# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

# Add a new task
def add_task(tasks, task_text):
    tasks.append({"task": task_text, "done": False})
    print(f"✅ Added: {task_text}")

# Delete a task by index
def delete_task(tasks, task_index):
    try:
        removed = tasks.pop(task_index)
        print(f"🗑️ Deleted: {removed['task']}")
    except IndexError:
        print("❌ Invalid task number.")

# List all tasks
def list_tasks(tasks):
    if not tasks:
        print("📭 No tasks found.")
    for i, t in enumerate(tasks):
        status = "✅" if t["done"] else "🔲"
        print(f"{i + 1}. {status} {t['task']}")

# Mark task as done
def mark_done(tasks, task_index):
    try:
        tasks[task_index]["done"] = True
        print(f"☑️ Marked as done: {tasks[task_index]['task']}")
    except IndexError:
        print("❌ Invalid task number.")

# Main loop
def main():
    tasks = load_tasks()
    while True:
        command = input("\nCommand (Add/List/Delete/Done/Save/Exit): ").strip().lower()
        if command == "add":
            task = input("Enter Task: ")
            add_task(tasks, task)
        elif command == "list":
            list_tasks(tasks)
        elif command == "delete":
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(tasks, index)
        elif command == "done":
            index = int(input("Enter task number to mark as done: ")) - 1
            mark_done(tasks, index)
        elif command == "save":
            save_tasks(tasks)
            print("💾 Tasks saved.")
        elif command == "exit":
            save_tasks(tasks)
            print("👋 Exiting. Tasks saved.")
            break
        else:
            print("⚠️ Unknown command.")

if __name__ == "__main__":
    main()
