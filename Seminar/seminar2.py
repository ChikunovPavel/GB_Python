# 1) Напишите программу, которая принимает на вход число N и выдаёт последовательность размера N из чередующихся по знаку степеней тройки.
# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81

n = int(input('input a number:'))
sum = 1
sum2 = 1

for i  in range(n):
    if i == 0:
        print(1)
    elif i % 2 != 0:
        sum = sum*3
        sum2 = sum*2
        sum2 = sum - sum2   
        print(sum2)
    else:
        sum = sum*3
        print(sum)
    




# 2) Напишите программу, в которой пользователь будет задавать две строки, одна из них - буква, а вторая фраза/слово,
# программа должна посчитать сколько раз буква встретилась буква во второй строке. (Не используя встроенные функции)


# 3) Петя и катя - брат и сестра. Петя - студент, а Катя - школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа, а Катя должна их отгадать
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P
# Помогите Кате отгадать задуманные Петей числа.

# *Пример*
# Ввод: 4 4
# Вывод: 2 2

# *Пример*
# Ввод: 5 6
# Вывод: 2 3