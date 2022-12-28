# Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.
# Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]
# Ввод: 4
# [-4, -3, -2, -1, 0, 1, 2, 3,4]

n = abs(int(input('input a number n:')))
array = []
for i in range(-n,n+1):
    array.append(i)
print(array)
a =array[int(input('input index a:'))]
b =array[int(input('input index b:'))]
c =array[int(input('input index c:'))]
d =array[int(input('input index d:'))]
e =array[int(input('input index e:'))]
print(a*b*c*d*e)
