import pytest
from lib.todo_list import TodoList
from unittest.mock import Mock
"""
When we add one todo
We get the todo back in the todos list
"""

def test_todolist_adds_one_todo_in_list():
    todo_list = TodoList()
    todo = Mock()
    todo_list.add(todo)
    assert todo_list.get_todos() == [todo]


"""
When we add one todo with an empty task
We get an error
"""

def test_todolist_adds_one_todo_with_empty_task_raises_exception():
    todo_list = TodoList()
    todo = Mock()
    todo.task = ""
    with pytest.raises(Exception) as e:
        todo_list.add(todo)
    assert str(e.value) == "Cannot add empty task to the tasklist"
