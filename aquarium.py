length = int(input())
width = int(input())
height = int(input())
percent = float(input()) / 100
volume = length * width * height / 1000
total_sum = volume - (percent * volume)
print(total_sum)