# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

# 2*x^2  + 4*x      5*x^2 + 2*x
#     7x^2 + 6x 

# 2*x^6  + 4*x      5*x^2 + 2*x
#     2*x^6 + 5x^2 + 6x

import re
import itertools

file1 = 'HomeWork/HomeWork4/str1.txt'
file2 = 'HomeWork/HomeWork4/str2.txt'
file_sum = 'HomeWork/HomeWork4/34_Sum_polynomials.txt'

def reader(file):
    with open(str(file),'r') as data:
            polynomial = data.readline()
    return polynomial


def convert(pol):
    pol = pol.replace('= 0', '') # замена символа на символ
    pol = re.sub("[*|^| ]", " ", pol).split('+') # возврашает новую строку 
    pol = [char.split(' ') for char in pol]
    pol = [[x for x in list if x] for list in pol]
    for i in pol:
        if i[0] == 'x': i.insert(0, 1)
        if i[-1] == 'x': i.append(1)
        if len(i) == 1: i.append(0)
    pol = [tuple(int(x) for x in j if x != 'x') for j in pol] # кортеж 
    return pol

def fold_pols(pol1, pol2):   
    x = [0] * (max(pol1[0][1], pol2[0][1] + 1))
    for i in pol1 + pol2:        
        x[i[1]] += i[0]
    res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
    res.sort(key = lambda r: r[1], reverse = True)
    return res        

def get_sum_pol(pol):
    var = ['*x^'] * len(pol)
    coefs = [x[0] for x in pol]
    degrees = [x[1] for x in pol]
    new_pol = [[str(a), str(b), str(c)] for a, b, c in (zip(coefs, var, degrees))] # берёт на вход несколько списков и создаёт из них список
    for x in new_pol:
        if x[0] == '0': del (x[0])
        if x[-1] == '0': del (x[-1], x[-1])
        if len(x) > 1 and x[0] == '1' and x[1] == '*x^': del (x[0], x[0][0])
        if len(x) > 1 and x[-1] == '1': 
            del x[-1]
            x[-1] = '*x'
        x.append(' + ')
    new_pol = list(itertools.chain(*new_pol))
    new_pol[-1] = ' = 0'
    return "".join(map(str, new_pol))

def write_to_file(file, pol):
    with open(file, 'w') as data:
        data.write(pol)

stro1 = reader(file1)
stro2 = reader(file2)
pol_1 = convert(stro1)
pol_2 = convert(stro2)

pol_sum = get_sum_pol(fold_pols(pol_1, pol_2))
write_to_file(file_sum, pol_sum)


print(stro1)
print(stro2)
print(pol_sum)

