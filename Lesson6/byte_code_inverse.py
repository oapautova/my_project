#!/usr/bin/python3
print("Для выхода и получения результата нажмите Enter")

byte_list = []

while True:
    num = input("Введите целое число, в диапазоне от 0 до 1114111: ")
    try:
        num = int(num)
        if 0 <= num <= 1114111:
            byte_list.append(num)
        else:
            print("Число должно быть в диапазоне от 0 до 1114111")
            continue
    except ValueError:
        if num == "":
            break
        else:
            print("Ввод не соответствует условию")
            continue


def inverse_bytes(*b):
    '''Перевод быйт кода в символы

    Принимает:
        байт код
    Возвращает:
        соответствующие байт коду символы

    '''

    symbol_list = []
    for x in b:
        symbol_list.append(chr(x))
    return symbol_list

print("Байт код:", byte_list)    
print("Соответствующие символы:", inverse_bytes(*byte_list))
