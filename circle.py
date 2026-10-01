import math


def area(r):
    '''
    функция вычисления площади окружности

принимает любое числовое значение (int|float|double|long|short) r 
возращает площадь окружности c радиусом r
    '''
    return math.pi * r * r


def perimeter(r):
'''
    функция вычисления длины окружности

принимает любое числовое значение (int|float|double|long|short) r 
возращает длину окружности c радиусом r
'''
    return 2 * math.pi * r

