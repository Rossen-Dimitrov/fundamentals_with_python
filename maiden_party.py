maiden_party_cost = float(input())
love_messages = int(input())
wax_roses = int(input())
key_holders = int(input())
caricature = int(input())
lucks = int(input())

love_messages_price = 0.60
wax_rose_price = 7.20
key_holders_price = 3.60
caricature_price = 18.20
lucks_price = 22

total = love_messages * love_messages_price + wax_roses * wax_rose_price\
        + key_holders * key_holders_price + caricature * caricature_price + lucks * lucks_price
if love_messages + wax_roses + key_holders + caricature + lucks >= 25:
    total *= 0.65

total *= 0.9
diff = abs(total - maiden_party_cost)
if total > maiden_party_cost:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")