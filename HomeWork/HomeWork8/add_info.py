import csv
 

def add_info(file):
    last_name = input('Введите фамилию ученика: ').capitalize() ## переводит первую букву в верхний регистр
    first_name = input('Введите имя ученика: ').capitalize() 
    with open(file, 'a', encoding = 'UTF-8', newline='') as data:
        fields = ['Фамилия', 'Имя', 'Класс', 'Литература', 'Русский язык', 'Математика', 'Физкультура', 'Информатика']
        writer = csv.DictWriter(data, fieldnames= fields)
        writer.writerow({'Фамилия': last_name, 'Имя': first_name})

def add_grades(file):
    subject = input('Введите название предмета: ').capitalize()
    grade = input('Введите оценку: ')
    number = int(input('Введите порядковый номер, указанный выше перед фамилией ученика: '))
    my_dict = []
    with open(file, 'r', encoding = 'UTF-8', newline='') as data:
        for row in csv.reader(data): ## возвращает объект reader, который построчно итерирует csvfile
            my_dict.append({'Фамилия': row[0], 'Имя': row[1], 'Литература': row[2], 'Русский язык': row[3], 'Математика': row[4],\
                      'Физкультура': row[5], 'Информатика': row[6],})
    my_dict[number][subject] += f'{grade} '
    with open(file, 'w', encoding = 'UTF-8', newline='') as data:
        fields = ['Фамилия', 'Имя', 'Литература', 'Русский язык', 'Математика', 'Физкультура', 'Информатика']
        writer = csv.DictWriter(data, fieldnames= fields)   #Класс DictWriter() модуля csv создает объект, 
                                                            #который работает как csv.writer(), но позволяет передавать строку с данными на запись как словарь,
                                                            #ключи которой задаются необязательным параметром fieldnames..
        writer.writerows(my_dict)