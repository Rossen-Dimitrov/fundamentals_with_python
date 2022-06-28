long = float(input())
width = float(input())

bura_long = long // 1.2
bura_width = (width - 1) // 0.7
total = bura_width * bura_long - 3

print(f"{total:.0f}")