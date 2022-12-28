# Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.
n = int(input('input a number n:'))
sum = 0
i = 1
while i <= n:
    if i % 2 == 0:
        sum = sum + i
        i = i + 1
    else:
        i = i + 1        
print(sum)        