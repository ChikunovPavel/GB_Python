# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list = []
size = int(input("input size list:"))
for i in range(size):
    list.append(int(input(f'input value list[{i}]:')))
    
count = len(list)  
if  count % 2 != 0:
    count = len(list) // 2+1
else:
    count = len(list) // 2

new_list = [list[i]*list[len(list)-i-1] for i in range (count)] 
print(new_list)

