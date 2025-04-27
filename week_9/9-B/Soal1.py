from collections import namedtuple

Koordinat = namedtuple('Koordinat', ['x', 'y'])

# b. Membuat instance dari namedtuple Koordinat
titik1 = Koordinat(x=2, y=4)

print(f"Elemen dengan indeks    : x = {titik1[0]}, y = {titik1[1]}")

print(f"Elemen dengan nama field: x = {titik1.x}, y = {titik1.y}")

print(f"Elemen dengan getattr   : x = {getattr(titik1, 'x')}, y = {getattr(titik1, 'y')}")