from todo_list import ToDoList
import view


def main_menu():
    ToDoList.create_from_csv()

    user_choice = ''
    while user_choice != 0:
        view.print_main_menu()
        user_choice = view.get_user_input()

        if user_choice == 1:
            # show all items
            pass

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


