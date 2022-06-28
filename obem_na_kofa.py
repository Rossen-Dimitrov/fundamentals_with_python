import time
from math import pi, cos, sin

d = float(input("Диаметър на дъното = "))
c = float(input("Височина на пиванта мъст = "))
b = cos(1.48353) * c
h = sin(1.48353) * c
r = (d / 2) + b
v = pi * r * r * h
print(f"Обем {v/1000:.2f} литра")
time.sleep(10)