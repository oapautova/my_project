#!/usr/bin/python3
print("Введите числа, которые необходимо сложить.") 
print("Для завершения ввода и получения результата нажмите Enter")

num_list = []
while True:
    num = input("Введите число: ")
    try:
        num = complex(num)
        num_list.append(num)
    except ValueError:
        if num == "":
            break
        print("Необходимо вводить только числа")

def add(*arg):
    summa = 0
    for x in arg:
        summa += x
    return summa

result = add(*num_list)
if result.imag == 0:
    result = result.real

print(f"Сумма всех введенных чисел: {result}")
