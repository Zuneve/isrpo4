import math

class Circle:
    def area(r):
        ''' Принимает число r, возвращает площадь круга с радиусом r'''
        if r > 0: 
            return math.pi * r * r
        else:
            return -1 

    def perimeter(r):
        ''' Принимает число r, возвращает длину окружности с радиусом r'''
        if r > 0:
            return 2 * math.pi * r
        else:
            return -1


class Rectangle:
    def area(a, b):
        '''Принимает числа a, b, возвращает площадь прямоугольника со сторонами a, b'''
        if a > 0 and b > 0:
            return a * b
        else:
            return -1

    def perimeter(a, b):
        '''Принимает числа a, b, возвращает периметр прямоугольника со сторонами a, b'''
        if a > 0 and b > 0:
            return 2 * a + 2 * b
        else:
            return -1


class Square:
    def area(a):
        '''Принимает число a, возвращает площадь квадрата со стороной a'''
        if a > 0: 
            return a * a
        else:
            return -1

    def perimeter(a):
        '''Принимает число a, возвращает периметр квадрата со стороной a'''
        if a > 0:
            return 4 * a
        else: 
            return -1


class Triangle:
    def area(a, h): 
        '''Принимает числа a, h, возвращает площадь треугольника 
        со стороной а и проведенной к ней высоте h'''
        if a > 0 and h > 0:
            return a * h / 2 
        else:
            return -1

    def perimeter(a, b, c): 
        '''Принимает числа a, b, c, возвращает периметр треугольника 
        со сторонами  a, b, c'''
        if a > 0 and b > 0 and c > 0:
            return a + b + c
        else:
            return -1
            
    def is_valid(a, b, c):
        '''Принимает числа a, b, c, возвращает true если треугольник 
        со сторонами  a, b, c существует'''
        if a <= 0 or b <= 0 or c <= 0:
            return False
        a, b, c = min(a, b, c), a + b + c - min(a, b, c) - max(a, b, c), max(a, b, c)
        return a + b < c
