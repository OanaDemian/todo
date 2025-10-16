from lib.todo_list import TodoList
from unittest.mock import Mock
"""
When we add one todo
We get the todo back in the todos list
"""

def test_adds_one_todo_in_list():
    todo_list = TodoList()
    todo = Mock()
    todo_list.add(todo)
    assert todo_list.get_todos() == [todo]