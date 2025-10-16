# File: lib/todo_list.py
class TodoList:
    def __init__(self):
        self._todos = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        if todo.task.strip() == "":
            raise Exception("Cannot add empty task to the tasklist")
        self._todos.append(todo)

    def get_todos(self):
        return self._todos

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        return [todo for todo in self._todos if not todo.complete]

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        return [todo for todo in self._todos if todo.complete]

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        pass