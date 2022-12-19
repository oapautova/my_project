#!/usr/bin/python3
a = input("Введите строку: ")

def byte(n):
    b = []
    for x in n:
        for y in x:
            b.append(ord(y)) 
    return b

b_cod = byte(a)
print("Список байт кодов введенной строки:", b_cod, sep='\n')
            
def invers_byte(c):
    d = []
    for f in c:
        d.append(chr(f))
    e = "".join(d)
    return e
        
print("Введенная строка:", invers_byte(b_cod), sep='\n')
