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

    @classmethod
    def create_from_csv(cls, csv_path):
        splitted_data = cls.get_data_from_file(csv_path)
        for text in splitted_data:
            todo_item = ToDoItem(text)
            cls.add_item(todo_item)

    @classmethod
    def get_data_from_file(cls, csv_path):
        with open(csv_path, 'r') as csvfile:
            splitted_rows = [line.strip() for line in csvfile]

        return splitted_rows

