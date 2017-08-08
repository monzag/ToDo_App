def print_main_menu():
    options = ['Show all items', 'Add new item', 'Mark item', 'Archive']
    get_list(options)
    print_exit_option()


def get_list(options):
    number = 1
    for option in options:
        print('{}. {}'.format(number, option))
        number += 1


def get_user_input():
    number = input('Choose option: ')
    if number.isdigit():
        return int(number)
    else:
        print('Must be integer!')


def print_exit_message():
    print('Good bye!:)')


def print_exit_option():
    print('0. Exit')


def get_new_item():
    return input('Write new item: ')
