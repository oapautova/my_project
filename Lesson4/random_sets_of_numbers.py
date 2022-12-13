#!/usr/bin/python3
from random import randint

a = [randint(-100, 100) for i in range(20)]
b = [randint(-100, 100) for i in range(20)]

c = set(a)
d = set(b)

print(f"набор случайных чисел a: {a}")
print(f"набор случайных чисел b: {b}")

difference_a_b = c - d
difference_b_a = d - c
union = difference_a_b | difference_b_a
print("элементы, входящие одновременно в наборы чисел a и b:", c & d)
print(f"элементы, входящие в набор чисел а, но не входящие в набор чисел b: {difference_a_b}")
print(f"элементы, входящие в набор чисел b, но не входящие в набор чисел a: {difference_b_a}")
print(f"элементы, входящие только в набор чисел a и только в набор чисел b: {union}")
