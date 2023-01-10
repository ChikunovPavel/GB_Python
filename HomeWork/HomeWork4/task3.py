# Задайте последовательность чисел. Напишите программу, которая выведет список элементов, которые не имели повторов в исходной последовательности.
# Ввод:
# 3 1 2 3
# Вывод:
# 2 1

list = input("Enter numbers separated by spaces ").split()
# list = [12,12,32,12,1,2,3,32,14,15,15]
newlist =[]
print(list)
for i in list:
    num = 0
    for j in list:
        if [j] == [i]:
            num +=1
    if num == 1:
        newlist += [i]
print(newlist)
            