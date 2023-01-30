import csv

def search_word(word):
    with open('journal.csv', encoding='UTF-8') as data:
        file_reader = csv.DictReader(data, delimiter=',')#Класс DictReader() модуля csv создает объект, который работает как обычный reader(),
                                                            # но отображает информацию о каждой строке в качестве словаря dict, ключи которого задаются необязательным параметром fieldnames.
                                                            #delimiter — разделитель столбцов в строке CSV-файла
        total = 0
        count = 0
        for line in file_reader:
            if word in line['Фамилия']:
                print(f"{total + 1}.{line['Фамилия']} {line['Имя']}")
                count += 1
            total += 1
                
        
        
def search_grades():
    with open('journal.csv', encoding='UTF-8') as data:
        file_reader = csv.DictReader(data, delimiter=',')
        number = int(input('Введите порядковый номер, указанный выше перед фамилией ученика: '))
        subject = input('Введите название предмета или слово "все", если хотите посмотреть оценки по всем предметам: ').capitalize()
        count = 1
        if subject == 'Все':
            for line in file_reader:
                if number == count:
                    print(f"Литература: {line['Литература']}\nРусский язык: {line['Русский язык']}\nМатематика: {line['Математика']}\nФизкультура: {line['Физкультура']}")
                    print(f"Информатика: {line['Информатика']}")
                count += 1
        else: 
            for line in file_reader:
                if number == count:
                    print(f'{subject}: {line[subject]}')
                count += 1