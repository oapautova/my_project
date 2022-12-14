#!/usr/bin/python3
print("Вас приветствует функция сложения чисел. Введите числа, которые необходимо сложить. Для завершения ввода и получения результата введите 'выход'")

l = []
while True:
    a = input("Введите число: ")
    try:
        a = complex(a)
        l.append(a)
    except:
        if a == "выход":
            break
        print("Необходимо вводить только числа")

def func(*num):
    summa = 0
    for x in num:
        summa += x
    return summa

result = func(*l)
if result.imag == 0:
    result = result.real

print(f"Сумма всех введенных чисел: {result}")
