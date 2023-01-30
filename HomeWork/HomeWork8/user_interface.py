from add_info import add_info, add_grades
from search import search_word, search_grades


def menu():
    flag = input('Введите 0, чтобы продолжить, или любой другой символ, чтобы прервать работу программы... ')
    
    while flag == '0':
        print('Введите цифру, соответствующую правам доступа:')
        flag = input('1 - учитель\n2 - ученик\n')

        if flag == '1':
            print('Введите цифру, соответствующую действию: ')
            choice = int(input('1 - ввести данные об ученике\n 2 - внести оценки\n 3 - поиск информации\n'))

            if choice == 1:
                    add_info('journal.csv')
            elif choice == 2:
                last_name = input('Введите фамилию ученика с большой буквы, которому Вы хотите выставить оценку: ')
                search_word(last_name)
                add_grades('journal.csv')
            elif choice == 3:
                last_name = input('Введите фамилию ученика с большой буквы: ')
                search_word(last_name)
                search_grades('journal.csv')
        else:
            last_name = input('Введите свою фамилию с большой буквы: ')
            search_word(last_name)
            search_grades()
        flag = input('Введите 0, чтобы продолжить, или любой другой символ, чтобы прервать работу программы... ')
    print('Программа завершена.')