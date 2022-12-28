# 1) Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int (input('input a number n:'))
product = 1
a = []
for i in range (n):
    product = product*(i+1)
    a.append(product)
print(a)

