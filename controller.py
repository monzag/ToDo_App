from todo_list import ToDoList
import view


def main_menu():
    user_choice = ''
    while user_choice != 0:
        view.print_main_menu()
        user_choice = view.get_user_input()

        if user_choice == 1:
            pass

        elif user_choice == 2:
            pass

        elif user_choice == 3:
            pass

        elif user_choice == 4:
            pass

    view.print_exit_message()