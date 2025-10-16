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

"""
When we 3 todos
Then mark one as complete
#incomplete returns a list of the 2 uncompleted todos
"""

def test_todolist_incomplete():
    todo_list = TodoList()
    todo_1 = Mock("Feed the tarantula!")
    todo_2 = Mock("Buy more food for the spider")
    todo_3 = Mock("Clean the spider's den")
    todo_1.task = "Feed the tarantula!"
    todo_2.task = "Buy more food for the spider"
    todo_3.task = "Clean the spider's de"
    todo_1.complete = False
    todo_2.complete = False
    todo_3.complete = False
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    todo_list.add(todo_3)
    todo_1.complete = True
    assert todo_list.incomplete() == [todo_2, todo_3]

"""
When we 3 todos
Then mark one as complete
#complete returns a list of the completed todo
"""

def test_todolist_complete():
    todo_list = TodoList()
    todo_1 = Mock("Feed the tarantula!")
    todo_2 = Mock("Buy more food for the spider")
    todo_3 = Mock("Clean the spider's den")
    todo_1.task = "Feed the tarantula!"
    todo_2.task = "Buy more food for the spider"
    todo_3.task = "Clean the spider's de"
    todo_1.complete = False
    todo_2.complete = False
    todo_3.complete = False
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    todo_list.add(todo_3)
    todo_1.complete = True
    assert todo_list.complete() == [todo_1]