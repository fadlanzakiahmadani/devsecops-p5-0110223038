
import pytest

from app import add_task, list_tasks
from storage import TaskStorage
from validators import validate_title


def test_add_and_list_task(tmp_path):
    storage = TaskStorage(str(tmp_path / "tasks.json"))

    task = add_task(storage, "Complete security report")

    assert task.task_id == 1
    assert task.title == "Complete security report"
    assert len(list_tasks(storage)) == 1


def test_reject_empty_title():
    with pytest.raises(ValueError):
        validate_title("   ")


def test_reject_title_over_120_characters():
    with pytest.raises(ValueError):
        validate_title("x" * 121)


def test_task_ids_increment(tmp_path):
    storage = TaskStorage(str(tmp_path / "tasks.json"))

    first = add_task(storage, "First task")
    second = add_task(storage, "Second task")

    assert first.task_id == 1
    assert second.task_id == 2
