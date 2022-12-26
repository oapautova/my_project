#!/usr/bin/python3

import time

def sleep_decorator(func):
    """Ограничевает частоту вызова функции интервалом 1 раз в 10 секунд"""
    count = [0]
    last_call = [time.time()]
    def wrapper(x):
        if count[0] == 0:
            count[0] += 1
            return func(x)
        else:
            if time.time() - last_call[0] < 10:
                print(f'Результат будет выведен через {10 - (time.time() - last_call[0])} секунд')
                time.sleep(10 - (time.time() - last_call[0]))
        count[0] += 1
        last_call[0] = time.time()
        return func(x)
    return wrapper



@sleep_decorator
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
        return factor
    except:
        return print("Вводятся только целые числа больше 0")


while True:
    try:
        num = int(input('Введите целое число больше 0: '))
        if num < 1:
            print('Введено не корректное значение')
            quit()
        print(fact(num))
    except ValueError:
        print('Необходимо ввести целое число больше 0')
