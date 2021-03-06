def print_main_menu():
    options = ['Show all items', 'Add new item', 'Mark item', 'Archive']
    get_list(options)
    print_exit_option()


def get_list(options):
    number = 1
    print('')
    for option in options:
        print('{}. {}'.format(number, option))
        number += 1


def get_user_input():
    try:
        number = int(input('\nChoose option: '))

    except TypeError:
        print('\nMust be integer!\n')
        number = None

    finally:
        return number


def print_exit_message():
    print('\nGood bye!:)')


def print_exit_option():
    print('0. Exit')


def get_new_item():
    return input('\nWrite new item: ')
