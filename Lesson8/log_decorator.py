#!/usr/bin/python3
import logging

def log_decorator(func):
    """Записывает логи выполняемой функции в файл py_log.log"""
    def wrapper(x):
        func(x)
        logging.basicConfig(level=logging.INFO, filename="py_log.log", format="%(asctime)s %(levelname)s %(message)s")
        logging.info(f'The value of x {x}')
        try:
            x = float(x)
            logging.info (f'square x = {x ** 2}')
        except ValueError:
            logging.error ('ValueError')
    return wrapper

@log_decorator
def square(x):
    try:
        x = float(x)
        return print(f'Квадрат числа равен {x ** 2}')
    except ValueError:
        return print(f'Необходимо вводить только числа')

num = input("Введите число:")
square(num)
