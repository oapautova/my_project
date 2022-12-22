#!/usr/bin/python3
def fibonacci(n):
    """Числа Фибоначчи

    Принимает:
        Номер элемента последовательности Фибоначчи
    Возвращает:
        Значение элемента последовательности
   
    """

    if n == 0:
        return n
    elif n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print ("Вводится целое положительное число.")
print()
try:
    a = int(input("Введите номер элемента последовательности Фибоначчи: "))
except ValueError:
    a = -1

if a >= 0:
    print(f"число Фибоначчи: {fibonacci(a)}")
else:
    print("Ведены не корректные данные.")
