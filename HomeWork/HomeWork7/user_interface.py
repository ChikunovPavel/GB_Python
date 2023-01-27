from os.path import exists
from scv_creating import creating
from view import writing_scv, writing_txt, get_info
from export import from_file


def view():
    print(from_file('HomeWork/HomeWork7/Phonebook.txt'))


def record_info():
    info = get_info()
    writing_scv(info)
    writing_txt(info)


def choice():
    flag = input(
        'Press \'yes\' to continue, or any character to quit... ')
    while (flag.lower() == 'yes'):
        path = 'HomeWork/HomeWork7/Phonebook.csv'
        valid = exists(path)
        if not valid:
            creating()
        choice_action = input(
            'Enter \'yes\' if you want to write new data, and any other character if you want to view the directory in the console:')
        if choice_action.lower() == 'yes':
            record_info()
        else:
            view()
        flag = input(
            'Press \'yes\' to continue, or any character to quit... ')
    print('The program has ended.')