#!/usr/bin/python3
from random import randint

a = [randint(-100, 100) for i in range(20)]
print(f"случайная последовательность: {a}")

for i in range(len(a) - 1):
    count = 0
    for j in range(len(a) - i - 1):
        if a[j] > a[j + 1]:
            a[j],a[j + 1] = a[j + 1],a[j]
            count += 1
    if count == 0:
        break

print(f"сортировка по возрастанию:    {a}")
