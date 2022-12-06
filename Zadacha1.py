# Вычислить число Пи c заданной точностью d

import math

d = input('Введите число: ')

def separate_fraction(num: float) -> float:
    """Возвращает количество знаков после . """ 
    list_num = str(num).split('.')      
    return len(list_num[1])      


print(round(math.pi, separate_fraction(d)))