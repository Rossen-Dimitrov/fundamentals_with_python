#1. импортиране на числото Пи.
from math import pi

#2. четене от конзолаа стойност за радиани.
radians = float(input('radians = '))

#3. Пресмятане на градусите.
degrees = radians * 180 / pi
#4. Принтиране на градусите.
print(degrees)