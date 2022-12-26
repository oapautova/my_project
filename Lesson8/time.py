#!/usr/bin/python3
import time

def time_decorator(func):
    def wrapper(x):
        "Выводит время выполнения функции"
        start = time.time()
        func(x)
        end = time.time()
        print(f'Время расчета: {end - start}')
        return  func
    return wrapper

@time_decorator
def fact(n):
    """факториал

    Принимает:
        целое положительное число
    Возвращает:
        факториал числа

    """

    factor = 1
    try:
        n = int(n)
        if n < 1:
            quit() 
        while n > 1:
            factor *= n
            n -= 1
        return print(factor)
    except:
        return print("Вводятся только целые числа больше 0")
        
num = input('Введите целое число больше 0: ')
fact(num)
