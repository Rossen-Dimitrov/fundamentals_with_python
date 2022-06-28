chicken_menu = int(input())
fish_menu = int(input())
vegan_menu = int(input())

chicken_menu_price = 10.35
fish_menu_price = 12.40
vegan_menu_price = 8.15
delivery = 2.5

food_price = chicken_menu_price * chicken_menu + fish_menu_price * fish_menu + vegan_menu_price * vegan_menu

desert = food_price * 0.2
total_price = food_price + desert + delivery
print(total_price)
