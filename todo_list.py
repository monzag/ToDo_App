from todo_item import ToDoItem
import csv


class ToDoList:

    def __init__(self):
        self.list_of_items = []

    def add_item(self, item):
        self.list_of_items.append(item)

    def mark_item(self, index):
        self.list_of_items[index].mark()

    def archive(self):
        for item in self.list_of_items:
            if item.is_done is True:
                self.list_of_items.remove(item)

    @classmethod
    def create_from_csv(cls, csv_path):
        todo_list = ToDoList()
        splitted_data = cls.get_data_from_file(csv_path)
        for row in splitted_data:
            text = row[0]

            # more than one column in file
            if len(row) > 1:
                todo_item = ToDoItem(text, True)
            else:
                todo_item = ToDoItem(text)

            todo_list.add_item(todo_item)

        return todo_list

    @classmethod
    def get_data_from_file(cls, csv_path):
        with open(csv_path, 'r') as csvfile:
            splitted_rows = [line.strip().split(',') for line in csvfile]

        return splitted_rows

    def save_data_to_file(self, file_name):
        list_to_save = self.get_data_to_save()

        with open(file_name, 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')

            for line in list_to_save:
                writer.writerow(line)

    def get_data_to_save(self):
        data_to_save = []

        for item in self.list_of_items:
            name = item.name
            if item.is_done is True:
                row = [name, 'done']
            else:
                row = [name]

            data_to_save.append(row)

        return data_to_save

