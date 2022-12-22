#!/usr/bin/python3
def prod(*num):
    """Произведение чисел

    Принимает:
        Любое количество чисел
    Возвращает:
        Произведение всех поданных на вход чисел

    """
    product = 1

    for x in num:
        product *= x
    return product

def thrice(y):
    """Умножение на 3

    Принимает:
        Число
    Возвращает:
        Принятое на вход число, умноженное на 3

    """ 
    return y * 3  

if __name__ == "__main__":
    print("Hello")
