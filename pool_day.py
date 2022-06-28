import math
people = int(input())
entrnace = float(input())
sunbed_price = float(input())
sun_umbrella_price = float(input())

sunbed = math.ceil(people * 0.75)
total = (people * entrnace) + (sun_umbrella_price * math.ceil(people / 2 )) + (sunbed_price * sunbed)
print(f"{total:.2f} lv.")

