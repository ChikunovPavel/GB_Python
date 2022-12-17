# 1.Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет


# a = int(input('input a day:'))

# if a == 6 or 7:
#     print('yes')
# else:
#     print('no')    


# 2.(!!!Доп!!!) Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# (0,0,0), (0,0,1) и тд.

def inputNumbers(x):
    xyz = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f"input value {xyz[i]}: "))
  


def checkPredicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result


statement = inputNumbers(3)

if checkPredicate(statement) == True:
    print(f"true")
else:
    print(f"false")



# 3.Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# x = float(input('input of coordinates x:'))
# y = float(input('input of coordinates y:'))

# if x > 0 and y > 0:
#     print('1 plane')
# elif x < 0 and y > 0:
#     print('2 plane')
# elif x < 0 and y < 0:
#     print('3 plane')
# elif x > 0 and y < 0:
#     print('4 plane')


# 4.Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# plane = int(input('plane number entry:'))

# if plane == 1:
#     print('x = from 0 to Ꚙ   and y = from 0 to Ꚙ ')
# elif plane == 2:
#     print('x = from 0 to -Ꚙ   and y = from 0 to Ꚙ')
# elif plane == 3:
#     print('x = from 0 to -Ꚙ   and y = from 0 to -Ꚙ')
# elif plane == 4:
#     print('x = from 0 to Ꚙ   and y = from 0 to -Ꚙ')


# 5.Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
# from math import sqrt
# from math import *


# xa = float(input('input of coordinates x point A:' ))
# ya = float(input('input of coordinates y point A:' ))1
# xb = float(input('input of coordinates x point B:' ))
# yb = float(input('input of coordinates y point B:' ))

# sum = (xb - xa)**2 + (yb - ya)**2

# print(round(sqrt(sum),3))



