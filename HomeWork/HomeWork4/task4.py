# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и вывести многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 
# k = 6
#     ix^6 + ax^5 + bx^4+ cx^3 + dx^2 + ex + h
#     a, b, c, d, e, h - рандом

from random import randint
import random


k = int(input("enter the degree of the polynomial:"))

a,b,c,d,e,h = (int(randint(0,100)) for _ in range(6)) 
list = [a,b,c,d,e,h]
str =''
for i in reversed(range(k+1)):
    if i != 1 and i != 0:
        str += f'{random.choice(list)}x^{i} + '
    elif i == 1:
        str += f'{random.choice(list)}x + '
    elif i == 0:
        str += f'{random.choice(list)}'
print(str)


