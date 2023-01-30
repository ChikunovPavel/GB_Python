import csv

def creating(file):
    with open(file, 'w', encoding = 'UTF-8', newline='') as data:
        fields = ['Фамилия', 'Имя', 'Литература', 'Русский язык', 'Математика', 'Физкультура', 'Информатика']
        writer = csv.DictWriter(data, fieldnames=fields)
        writer.writeheader()