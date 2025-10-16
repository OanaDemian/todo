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

