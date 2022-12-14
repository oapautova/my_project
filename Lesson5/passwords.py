#!/usr/bin/python3
print("Вводимый пароль должен содержать не менее 6 символов, должен содержать хотя бы одну цифру, не должен состоять только из цифр, не должен содержать слово 'password'.")
def func(c):
    d = 0
    for x in c:
        if x.isdigit():
            d += 1
    return d

while True:
    pas = input("Введите пароль:")
    a = len(pas)
    quantity_digit = func(pas)
    pas1 = pas.lower()
    s = pas1.find("password")
    if a < 6 or quantity_digit == a  or quantity_digit == 0 or s != -1:
        q = input("Пароль не корректный. Для выхода из программы введите 'выход', для повторного ввода пароля, нажмите enter или введите любой символ: ").lower().strip()
        if q == "выход":
            break
        else:
            continue
    else:
        print("Корректный пароль")
        quit()
