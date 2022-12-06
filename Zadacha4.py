# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.(записать в строку)

import random
import sympy
x = sympy.Symbol('x')

k = int(input('Введите значение k: '))
n = []
for i in range(k+1):
    a = random.randint(1, 10)*x**i 
    n.append(a)
    
n.reverse()

print(" + ".join(map(str,n)))
