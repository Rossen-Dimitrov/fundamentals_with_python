movie_name = str(input())   # 1.	Име на филм - текст
days = int(input())    # 2.	Брой дни - цяло число в диапазона [1… 90]
tickets_number = int(input())    # 3.	Брой билети  - цяло число в диапазона [100… 100000]
tickets_price = float(input())    # 4.	Цена на билет - реално число в диапазона [5.0… 25.0]
cinema_share = int(input())     # 5.	Процент за киното - цяло число в диапазона [5... 35]
total = (days * tickets_number * tickets_price)
incomes = total - ((total * cinema_share) / 100)
print(f"The profit from the movie {movie_name} is {incomes:.2f} lv.")