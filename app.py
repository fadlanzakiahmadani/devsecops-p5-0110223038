import argparse

from model import Task
from security import sanitize_task_title
from storage import TaskStorage


def add_task(storage: TaskStorage, title: str) -> Task:
    safe_title = sanitize_task_title(title)
    tasks = storage.load()

    next_id = max((task.task_id for task in tasks), default=0) + 1
    task = Task(task_id=next_id, title=safe_title)

    tasks.append(task)
    storage.save(tasks)
    return task


def list_tasks(storage: TaskStorage) -> list[Task]:
    return storage.load()


def main() -> None:
    parser = argparse.ArgumentParser(description="SecureTask task manager")
    parser.add_argument(
        "--data",
        default="tasks.json",
        help="Path to the JSON data file",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a task")
    add_parser.add_argument("title", help="Task title")

    subparsers.add_parser("list", help="List all tasks")

    args = parser.parse_args()
    storage = TaskStorage(args.data)

    try:
        if args.command == "add":
            task = add_task(storage, args.title)
            print(f"Added task {task.task_id}: {task.title}")
        elif args.command == "list":
            tasks = list_tasks(storage)
            if not tasks:
                print("No tasks found.")
            for task in tasks:
                status = "done" if task.completed else "pending"
                print(f"{task.task_id}. {task.title} [{status}]")
    except (ValueError, OSError) as error:
        parser.exit(1, f"Error: {error}\n")


if __name__ == "__main__":
    main()