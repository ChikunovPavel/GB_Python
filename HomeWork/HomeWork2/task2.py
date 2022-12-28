#  Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.
# Пример:
# Для n = 15: Ответ: 3
# Для n = 35: Ответ: 5

n = int(input('input a number n:'))
denominator = 2
while n % denominator != 0:
    if n % denominator != 0:
        denominator = denominator + 1
else:
    print(denominator)