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
    def create_from_csv(cls, file_path):
        pass

    @classmethod
    def get_data_from_file(cls, csv_path):
        with open(csv_path, 'r') as csvfile:
            splitted_rows = [line.strip().split(',') for line in csvfile]

        return splitted_rows
