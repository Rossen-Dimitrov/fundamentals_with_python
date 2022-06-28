skumria_price = float(input()) # •	Първи ред – цена на скумрията на килограм. Реално число в интервала [0.00…40.00]
caca_price = float(input()) # •	Втори ред – цена на цацата на килограм. Реално число в интервала [0.00…30.00]
palamud_kg = float(input()) # •	Трети ред – килограма паламуд. Реално число в интервала [0.00…50.00]
safrid_kg = float(input()) # •	Четвърти ред – килограма сафрид. Реално число в интервала [0.00… 70.00]
midi_kg = float(input())# •	Пети ред – килограма миди. Цяло число в интервала [0 ... 100]

palamud_price = skumria_price * 1.6
safrid_price = caca_price * 1.8
midi_price = 7.5
total = palamud_price * palamud_kg + safrid_price * safrid_kg + midi_price * midi_kg
print(f'{total:.2f}')