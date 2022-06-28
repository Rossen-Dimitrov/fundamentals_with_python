movie = str(input())# •	Първи ред - прожекция - текст с възможности"John Wick", "Star Wars" или "Jumanji"
packet = str(input())# •	Втори ред - пакет за филм - текст  с възможности "Drink", "Popcorn" или "Menu"
tickets = int(input())# •	Трети ред - брой билети - цяло число в интервала [1… 30]
price = 0

if movie == "John Wick":
    if packet == "Drink":
        price = 12
    elif packet == "Popcorn":
        price = 15
    else:
        price = 19
elif movie == "Star Wars":
    if packet == "Drink":
        price = 18
    elif packet == "Popcorn":
        price = 25
    else:
        price = 30
    if tickets >= 4:
        price *= 0.7
elif movie == "Jumanji":
    if packet == "Drink":
        price = 9
    elif packet == "Popcorn":
        price = 11
    else:
        price = 14
    if tickets == 2:
        price *= 0.85

price = price * tickets
print(f"Your bill is {price:.2f} leva.")