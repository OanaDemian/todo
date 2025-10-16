import pytest
from lib.todo import Todo

"""
When I initialize with a task to be done
I get that task back
"""

def test_constructs_and_gets_task():
    todo = Todo("buy a present for my mum")
    assert todo.task == "buy a present for my mum"

"""
When I initialize with a task to be done
Its complete status is False
"""


def test_constructs_and_gets_False_for_task_complete():
    todo = Todo("buy a present for my mum")
    assert todo.complete == False


"""
When I initialize with a task to be done
Then I mark the task complete
Its complete status is True
"""


def test_constructs_and_gets_True_for_task_complete_after_marking_task_complete():
    todo = Todo("buy food for my pet tarantula")
    todo.mark_complete()
    assert todo.complete == True

"""
When I initialize with a task to be done
Then I initialize another task to be done
Then I mark the first task complete
The first task's complete status is True
And the second tasks complete status is False
"""


def test_constructs_two_todos_mark_first_complete_checks_complete_status_for_both():
    todo_1 = Todo("buy food for my pet tarantula")
    todo_2 = Todo("clean the spider webs")
    todo_1.mark_complete()
    assert todo_1.complete == True
    assert todo_2.complete == False

"""
When task is an empty string
#mark_todo raises an error
"""

def test_mark_complete_when_empty_task_given():
    todo = Todo("   ")
    with pytest.raises(Exception) as e:
        todo.mark_complete()
    assert str(e.value) == "No task given. Add a new task!"
