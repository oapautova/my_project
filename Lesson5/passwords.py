#!/usr/bin/python3

print("Вводимый пароль должен содержать не менее 6 символов.")
print("Должен содержать хотя бы одну цифру.") 
print("Не должен состоять только из цифру") 
print("не должен содержать слово 'password'.")

def num_dig(c):
    """Считает количество цифр

    Пинимает:
        строку
    Возвращает:
        количество цифр в строке
    
    """

    d = 0
    for x in c:
        if x.isdigit():
            d += 1
    return d

while True:
    pas = input("Введите пароль:")
    lenght = len(pas)
    quantity_digit = num_dig(pas)
    pas1 = pas.lower()
    s = pas1.find("password")
    if lenght < 6 or quantity_digit == lenght  or quantity_digit == 0 or s != -1:
        print("Пароль не корректный. Для выхода из программы введите 'выход'.")
        print("для повторного ввода пароля, нажмите enter или введите любой символ:")
        q = input().lower().strip()
        if q == "выход":
            break
        else:
            continue
    else:
        print("Корректный пароль")
        quit()
