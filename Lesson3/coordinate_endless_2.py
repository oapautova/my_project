#!/usr/bin/python3
print("Ваши координаты 0:0")
x = 0; y = 0
go = "ДА"
while go == "ДА":
    try:
        x += float(input("Введите перемещение по оси x: "))
        y += float(input("Введите перемещение по оси y: "))
        print(f"Ваши координаты: {x}:{y}")
    except:
        print('Необходимо вводить только числа. Попробуй еще раз!')
    go = input("Чтобы продолжить, введите 'да': ").upper()
