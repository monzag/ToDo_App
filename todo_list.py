from todo_item import ToDoItem


class ToDoList:

    list_of_items = []

    def __init__(self):
        self.title = 'Your planner'

    @classmethod
    def add_item(cls, item):
        cls.list_of_items.append(item)

    @classmethod
    def mark_item(cls, item):
        return item.mark

    @classmethod
    def archive(cls, item):
        if item in cls.list_of_items:
            cls.list_of_items.remove(item)


