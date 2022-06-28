number_of_painted_egsg = int(input())
red = 0
orange = 0
blue = 0
green = 0
max_colour = ""
max_number = 0
for n in range(number_of_painted_egsg):
    colour_input = str(input())
    if colour_input == "red":
        red += 1
        if red > max_number:
            max_number = red
            max_colour = colour_input
    elif colour_input == "blue":
        blue += 1
        if blue > max_number:
            max_number = blue
            max_colour = colour_input
    elif colour_input == "green":
        green += 1
        if green > max_number:
            max_number = green
            max_colour = colour_input
    elif colour_input == "orange":
        orange += 1
        if orange > max_number:
            max_number = orange
            max_colour = colour_input
print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")
print(f"Max eggs: {max_number} -> {max_colour}")
