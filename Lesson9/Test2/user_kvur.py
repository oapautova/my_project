#!/usr/bin/python3

import kvur

print("Решение квадратного уровнения ax\u00B2 + bx + c = 0") 
print("Введите коэффициенты") 

a = input("a = ") 
b = input("b = ") 
c = input("c = ")

if kvur.check_cf(a, b, c):
    if kvur.discriminant(a, b, c) == 0:
        print('В уравнении 1 корень: x =', kvur.root_x1(a, b,c))
    else:
        print("В уравнении 2 корня")     
        print('x1= ', kvur.root_x1(a, b, c))
        print('x2= ', kvur.root_x2(a, b, c))
else:
    print('Необходимо вводить только числа! Коэффициент a не должен быть равен 0')
