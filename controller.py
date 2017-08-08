from todo_list import ToDoList
from todo_item import ToDoItem
import view


def main_menu():
    ToDoList.create_from_csv('todo_items.csv')

    user_choice = ''
    while user_choice != 0:
        view.print_main_menu()
        user_choice = view.get_user_input()

        if user_choice == 1:
            show_all_items()

        elif user_choice == 2:
            # add new item
            pass

        elif user_choice == 3:
            # mark item
            pass

        elif user_choice == 4:
            # archive
            pass

    view.print_exit_message()


def show_all_items():
    view.get_list(ToDoList.list_of_items)


def add_new_item():
    name = view.get_new_item()
    todo_item = ToDoItem(name)
    if todo_item not in ToDoList.list_of_items:
        ToDoList.add_item(todo_item)


def archive():
    for item in ToDoList.list_of_items:
        if item.is_done is True:
            ToDoList.list_of_items.remove(item)





