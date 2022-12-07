#!/usr/bin/python3
print("Ваши координаты 0:0")
try:
    x = float(input("Введите перемещение по оси x: "))
    y = float(input("Введите перемещение по оси y: "))
except:
    print("Необходимо воодить только числа!")
    quit()
print(f"Ваши координаты: {x}:{y}") 
