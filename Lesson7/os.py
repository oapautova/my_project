#!/usr/bin/python3
import os

name = os.name
user = os.getlogin()
files = os.listdir(path='.')

print(f"Имя операционной системы: {name}")
print(f"Имя пользователя, вошедшего в терминал: {user}")
print(f"Список файлов и дерикторий в текущей дериктории:\n{files}") 

