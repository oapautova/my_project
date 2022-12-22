#!/usr/bin/python3
import cmath
print("Решение квадратного уровнения ax\u00B2 + bx + c = 0")
print("Введите коэффициенты")
try:
    a = complex(input("a = "))
    b = complex(input("b = "))
    c = complex(input("c = "))
except:
    print('Необходимо вводить только числа!')
    quit()
if a.imag == 0:
    a = a.real
if b.imag == 0:
    b = b.real
if c.imag == 0:
    c = c.real
d = b**2 - (4*a*c)
if a == 0:
    print("a не может быть равен 0. Это не квадратное уравнение!")
elif d == 0:
    print("В уравнении 1 корень: x =", -b / (2*a))
else:
    print("В уравнении 2 корня")
    print("x1 = ", (-b + d**0.5) / (2*a))
    print("x2 = ", (-b - d**0.5) / (2*a))
