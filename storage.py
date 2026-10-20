import json
from pathlib import Path

from model import Task


class TaskStorage:
    def __init__(self, path: str = "tasks.json"):
        self.path = Path(path)

    def load(self) -> list[Task]:
        if not self.path.exists():
            return []

        with self.path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("Invalid task data format")

        return [Task.from_dict(item) for item in data]

    def save(self, tasks: list[Task]) -> None:
        data = [task.to_dict() for task in tasks]
        self.path.parent.mkdir(parents=True, exist_ok=True)

        with self.path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)