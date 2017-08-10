from todo_list import ToDoList
from todo_item import ToDoItem
import view


def main_menu():
    todo_list = ToDoList.create_from_csv('todo_items.csv')

    user_choice = ''
    while user_choice != 0:
        view.print_main_menu()
        user_choice = view.get_user_input()

        if user_choice == 1:
            show_all_items(todo_list)

        elif user_choice == 2:
            add_new_item(todo_list)

        elif user_choice == 3:
            mark_item(todo_list)

        elif user_choice == 4:
            todo_list.archive()

        todo_list.save_data_to_file('todo_items.csv')

    view.print_exit_message()


def show_all_items(todo_list):
    view.get_list(todo_list.list_of_items)


def add_new_item(todo_list):
    name = view.get_new_item()
    todo_item = ToDoItem(name)
    todo_list.add_item(todo_item)


def mark_item(todo_list):
    show_all_items()
    user_choice = view.get_user_input()
    if user_choice in range(len(todo_list.list_of_items) + 1):
        todo_list.mark_item(user_choice - 1)


