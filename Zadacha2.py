# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

n = int(input('Введите число: '))
a = []
i = 2
while n != 1:
    if n % i == 0:
        a.append(i)
        n = n/i
    else:
        i+=1

a[:] = set(a)
print (a)