#!/usr/bin/python3
invent = {'беговые лыжи': 1, 'футбольный мяч': 0.5, 'коньки': 1.5, 'гантели': 5,
     'обруч': 1, 'теннисная ракетка': 0.3, 'ласты': 0.5, 'сноуборд': 3, 
     'горные лыжи': 6, 'баскетбольный мяч': 0.7}

set = list(invent)
basket = {}

print("Вам доступен для выбора спортивный инвентарь из списка ниже:")
print()

for i in range(len(invent)):
    print(f"{set[i]} - {invent[set[i]]} кг")
print()    
print("Вы можете добавлять в корзину любой предмет в одном экземпляре.")
print("Вы можете удалить любой выбранный предмет из корзины") 
print("Вес корзины не может превышать 7 кг")

summa = 0

while summa <= 7:
    if summa == 7:
        print("Вес вашей корзины 7 кг, сейчас вы не можете добавлять предметы.")
    action = input("добавить/удалить/завершить:").lower()
    if action == "добавить":
        choice = input("введите название предмета, который хотите добавить:").lower()
        if choice in invent:
            summa += invent[choice]
            if summa <= 7:
               basket[choice] = invent[choice]
               set1 = list(basket)
               invent.pop(choice)
               for j in range(len(basket)):                 
                   print(f"{set1[j]} - {basket[set1[j]]} кг")
               print(f"вес вашей корзины = {summa} кг")
            else:
                summa -= invent[choice]
                print("Вы не можете добавить данный предмет. Превышен максимальный вес корзины.")
        else:
            if choice in basket:
                print("Данный предмет уже есть в Вашей корзине")
            else:
                print("Такого предмета нет")
            continue
    elif action == "удалить":
        choice = input("Введите название предмета, который хотите удалить:").lower()
        if choice in basket:
            summa -= basket[choice]
            invent[choice] = basket[choice]
            basket.pop(choice)
            set1 = list(basket)
            for k in range(len(basket)):
                print(f"{set1[k]} - {basket[set1[k]]} кг")              
            print(f"вес вашей корзины = {summa} кг")
        else:
            if choice in invent:
                print("Данного предмета нет в Вашей корзине")
            else:
                print("Нет такого предмета")
    elif action == "завершить":
        print("Ваша корзина:")
        for m in range(len(basket)):
            print(f"{set1[m]} - {basket[set1[m]]} кг")
        print("До свидания!")
        break
    else:
        print("Выберите из трех вариантов: добавить/удалить/завершить")
        continue
