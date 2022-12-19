#!/usr/bin/python3
l = []

while True:
    a = input("Введите целое число, в диапазоне от 0 до 1114111. Для выхода и получения результата нажмите Enter: ")
    try:
        a = int(a)
        if 0 <= a <= 1114111:
            l.append(a)
        else:
            print("Число должно быть в диапазоне от 0 до 1114111")
            continue
    except:
        if a == "":
            break
        else:
            print("Ввод не соответствует условию")
            continue


def inverse_bytes(*n):
    d = []
    for x in n:
        d.append(chr(x))
    return d

print("Байт код:", l)    
print("Соответствующие символы:", inverse_bytes(*l))
