bitcoin = int(input())
ch_uan = float(input())
commission = float(input()) / 100
usd = 1.76
euro = 1.95
bitcoin_price = 1168
ch_uan_price = 0.15 * usd

total = (bitcoin * bitcoin_price + ch_uan_price * ch_uan) / euro
commission = commission * total
total = total - commission
print(f'{total:.2f}')
