menu_chicken = int(input())
menu_fish = int(input())
menu_vegan = int(input())
chicken_menu_prise = 10.35 * menu_chicken
fish_menu_prise = 12.4 * menu_fish
vegan_menu_prise = 8.15 * menu_vegan
delivery_prise = 2.5
sum = chicken_menu_prise + fish_menu_prise + vegan_menu_prise
total_sum = sum * 1.2 + delivery_prise
print(f"Цена на поръчката {total_sum}лв.")
