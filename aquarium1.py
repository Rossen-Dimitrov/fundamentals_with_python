length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = (length * width * height) / 1000
total_volume = volume - (volume * percent / 100)
print(total_volume)
