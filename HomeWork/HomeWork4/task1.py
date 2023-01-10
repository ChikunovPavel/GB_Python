# Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков после запятой, сколько указал пользователь(БЕЗ round())
import math

print(math.pi)
b = int(input("enter the number of decimal places:"))
c = str(math.pi)
d = str()
if b == 0:
    print(c[0])
else:
    for i in range (b+2): 
        e = str(c[i])
        d = d +e 
    print(d)
