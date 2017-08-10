from todo_item import ToDoItem
import csv


class ToDoList:

    # utworzyć init, atrybut instancji
    list_of_items = []

    @classmethod
    def add_item(cls, item):
        cls.list_of_items.append(item)

    @classmethod
    def mark_item(cls, index):
        cls.list_of_items[index].mark()

    @classmethod
    def archive(cls, item):
        if item in cls.list_of_items:
            if item.is_done is True:
                cls.list_of_items.remove(item)

    @classmethod
    def create_from_csv(cls, csv_path):
        splitted_data = cls.get_data_from_file(csv_path)
        for row in splitted_data:
            text = row[0]

            if len(row) > 1:
                todo_item = ToDoItem(text, True)
            else:
                todo_item = ToDoItem(text)

            cls.add_item(todo_item)

    @classmethod
    def get_data_from_file(cls, csv_path):
        with open(csv_path, 'r') as csvfile:
            splitted_rows = [line.strip().split(',') for line in csvfile]

        return splitted_rows

    @classmethod
    def save_data_to_file(cls, file_name):
        list_to_save = cls.get_data_to_save()

        with open(file_name, 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')

            for line in list_to_save:
                writer.writerow(line)

    @classmethod
    def get_data_to_save(cls):
        data_to_save = []

        for item in cls.list_of_items:
            name = item.name
            if item.is_done is True:
                row = [name, 'done']
            else:
                row = [name]

            data_to_save.append(row)

        return data_to_save

