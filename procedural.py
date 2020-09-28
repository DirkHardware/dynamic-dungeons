# Pixel Art - http://www.101computing.net/pixel-art-in-python/
import structures

list = [1, 2, 3, "S"]

print(list.index("S"))

structure = structures.TeeHall()

for row in structure.layout:
    if "S" in row:
        print(row.index("S"))

