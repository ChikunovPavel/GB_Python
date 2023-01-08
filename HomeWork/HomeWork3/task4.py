# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

a = int(input("Enter a number to convert decimal to binary:\n"))
b = ""
while a != 0 :
    b =  str(a % 2) + b
    a //= 2
print(b)
   


