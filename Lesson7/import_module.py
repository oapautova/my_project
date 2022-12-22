#!/usr/bin/python3

import mult

print("Введите числа, которые необходимо умножить.") 
print("Для выхода и получения результата нажмите Enter.")

input_arg = []
while True:
    num = input("Введите число: ")
    try:
        num = complex(num)
        input_arg.append(num)
    except ValueError:
        if num == "":
            break
        print("Необходимо вводить только числа")

result = mult.prod(*input_arg)

if result.imag == 0:
    result = result.real


print(f"Произведение всех введенны чисел: {result}")
