#!/usr/bin/python3

string = input("Введите строку: ")

def byte(n):
    """Перевод символов в байт код

    Принимает:
        строку
    Возвращает:
        список байт кодов символов строки
 
    """
    byte_list = []
    for x in n:
        for y in x:
            byte_list.append(ord(y)) 
    return byte_list

result = byte(string)
print(f"Список байт кодов введенной строки:\n{result}")
            
def invers_byte(c):
    """Переводит байт код в символы"""
    symbol_list = []
    for f in c:
        symbol_list.append(chr(f))
    return_string = "".join(symbol_list)
    return return_string
        
print("Введенная строка:", invers_byte(result), sep='\n')
