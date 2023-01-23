# 3) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

def sum_digits(num):
    return sum(map(int, 0,num.replace('.','').replace('-','')))

num = input('enter a real number:')
print(f' dsaf {sum_digits(num)}')
