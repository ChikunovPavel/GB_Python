# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
# *Примеры:*
# - 5, 25 -> да
# - 25, 5 -> да
# - 8,9 -> нет

# print('input number a:')
# a = int(input())
# print('input number b:')
# b = int(input())

# if a == b**2 or b == a**2:
#     print('yes')
# else:
#     print('no')


# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90


# a = int(input('input number a:'))
# b = int(input('input number b:'))
# c = int(input('input number c:'))
# d = int(input('input number d:'))
# e = int(input('input number e:'))

# print(f'влфыао:{max(a,b,c,d,e)}')

#3.дано 3 значное число нужно найти сумму его цифр

# a = int(input('input three-digit number'))
# print((a % 100 // 10)+(a % 10)+(a // 100))
#  (вторая цифра) (третья цифра) (первая цифра)

# данны 2 числа проверить что первое делиться на второе без остатка

# a = int(input('input a number'))
# b = int(input('input a number'))
# if b !=0:
#     if(a % b == 0):
#         print('yes')
#     else:
#         print('no')
# else:
#     print('input')   



# 3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N5
# *Примеры:*
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5   

# a = abs(int(input('input a number')))

# for i in range(-a,a+1):
#      print(i, end = ' ' )


# 4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# *Примеры:*
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3  

# from math import*
# a = float(input('input'))

# if a - floor(a) !=0:
#     print(floor(a*10)%10)
# else:
#     print('no')
 
from math import*
a = float(input('input'))

if a - trunc(a) !=0:
    print(trunc(a*10)%10)
else:
    print('no')