#!/usr/bin/python3
from animals import human

class student(human):
    def __init__(self, age, wool, spine, weight, voice, herbivorous, limbs, breastfeeding, gender, name, height, speciality, GPA, homework):
        super().__init__(age, wool, spine, weight, voice, herbivorous, limbs, breastfeeding, gender, name, height)
        self.speciality = speciality
        self.GPA = GPA
        self.homework = homework
    def __lt__(self, other):
        return self.homework < other.homework
    def __gt__(self, other):
        return self.homework > other.homework
    def __eq__(self, other):
        return self.homework == other.homework



    

Марина = student(18, 'no', 'yes', 55, 'yes', 'yes', 4, 'yes', 'female', 'Марина', 167, 'Telecomunication', 4.2, 5)   
Владимир = student(19, 'no', 'yes', 75, 'yes', 'yes', 4, 'yes', 'male', 'Владимир', 180, 'Telecomunication', 4.5, 4)
Егор = student(18, 'no', 'yes', 70, 'yes', 'yes', 4, 'yes', 'male', 'Егор', 175, 'Telecomunication', 5, 7)
Алина = student(19, 'no', 'yes', 50, 'yes', 'yes', 4, 'yes', 'female', 'Алина', 160, 'Telecomunication', 4, 6)


def dz(name1, name2):
    '''Сравнивает количество баллов у студентов

    Принимает:
        Имена двух студентов
    Возвращает:
        Сравнение, у кого баллов больше.

    '''
    if name1 > name2:
        return f'У студента {name1.name}, больше баллов за домашнее задание чем у студента {name2.name}'
    elif name1 == name2:
        return f'У студентов {name1.name} и {name2.name} одинаковое количество баллов за домашнее задание'
    elif name1 < name2:
       return f'У студента {name2.name} больше баллов за домашнее задание чем у студента {name1.name}'

print(dz(Марина, Алина))
print(dz(Марина, Егор))
print(dz(Егор, Владимир))
