import pytest
from lib.todo import Todo
from lib.todo_list import TodoList

"""
When we add one todo
We get the todo back in the todos list
"""

def test_adds_one_todo_in_list():
    todo_list = TodoList()
    todo = Todo("feed the tarantulas")
    todo_list.add(todo)
    assert todo_list.get_todos() == [todo]

"""
When we add one todo with an empty task
We get an error
"""

def test_adds_one_todo_with_empty_task_raises_exception():
    todo_list = TodoList()
    todo = Todo("")
    with pytest.raises(Exception) as e:
        todo_list.add(todo)
    assert str(e.value) == "Cannot add empty task to the tasklist"

"""
When we 3 todos
Then mark one as complete
#incomplete returns a list of the 2 uncompleted todos
"""

def test_incomplete():
    todo_list = TodoList()
    todo_1 = Todo("Feed the tarantula!")
    todo_2 = Todo("Buy more food for the spider")
    todo_3 = Todo("Clean the spider's den")
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    todo_list.add(todo_3)
    todo_1.mark_complete()
    assert todo_list.incomplete() == [todo_2, todo_3]