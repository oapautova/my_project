#!/usr/bin/python3

line = input("Ввод: ")

last = line[len(line) - 1]
penult = line[len(line) - 2]

print(f"2 последних символа ввода, в обратном порядке: {last}{penult}")
