from todo_item import ToDoItem


class ToDoList:

    list_of_items = []

    def __init__(self):
        self.title = 'Your planner'

    @classmethod
    def add_item(cls, item):
        cls.list_of_items.append(item)

