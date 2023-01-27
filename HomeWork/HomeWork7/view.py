def get_info():
    info = []
    last_name = input('Enter last name: ')
    info.append(last_name)
    first_name = input('Enter your name: ')
    info.append(first_name)
    phone_number = ''
    valid = False
    while not valid:
        try:
            phone_number = input('Enter phone number: ')
            if len(phone_number) != 11:
                print('The phone number must contain 11 digits.')
            else:
                phone_number = int(phone_number)
                valid = True
        except:
            print('The phone number must contain only numbers.')
    info.append(phone_number)
    description = input('Enter a description: ')
    info.append(description)
    return info


def writing_scv(info):
    file = 'HomeWork/HomeWork7/Phonebook.csv'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'{info[0]};{info[1]};{info[2]};{info[3]}\n')


def writing_txt(info):
    file = 'HomeWork/HomeWork7/Phonebook.txt'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(
            f'Surname: {info[0]}\n\nName: {info[1]}\n\nPhone number: {info[2]}\n\nDescription: {info[3]}\n\n\n')