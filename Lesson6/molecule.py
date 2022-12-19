#!/usr/bin/python3
f = open("input.txt", "r")

r = f.read().split()
f.close()


C = int(r[0]) // 2
H = int(r[1]) // 6
O = int(r[2])

e = open('output.txt', 'w')
e.write(f"Максимальное количество молекул спирта: {min(C, H, O)}\n")
e.close()
