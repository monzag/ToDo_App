from todo_item import ToDoItem
import csv


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
        for row in splitted_data:
            text = row[0]
            is_done = row[1]
            todo_item = ToDoItem(text)
            todo_item.is_done = is_done

    @classmethod
    def get_data_from_file(cls, csv_path):
        with open(csv_path, 'r') as csvfile:
            splitted_rows = [line.strip().split(',') for line in csvfile]

        return splitted_rows

    @classmethod
    def save_data_to_file(cls):
        list_to_save = cls.get_data_to_save()
        file_path = cls.__class__.__name__ + '.csv'

        with open(file_path, 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')

            for line in list_to_save:
                writer.writerow(line)

    @classmethod
    def get_data_to_save(cls):
        data_to_save = []

        for item in cls.list_of_items:
            name = item.name
            is_done = item.is_done
            row = [name, is_done]
            data_to_save.append(row)

        return data_to_save

