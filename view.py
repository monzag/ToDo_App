def print_main_menu():
    options = []
    get_list(options)


def get_list(options):
    number = 1
    for option in options:
        print('{}. {}'.format(number, option))
        number += 1
