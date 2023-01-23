# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension


# 1) Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности
# оставшихся чисел в одну строчку через пробел.
# [1,2,3,4,22,234,24] ----> [22, 24]

def double_digit():
    num = list(map(int,input('Enter numbers separated by spaces').split()))
    return ' '.join(map(str,filter(lambda i: 9 < abs(i) < 100,num)))

print(f'[{double_digit()}]')