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