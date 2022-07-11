user_in = input()
dict_product = {}

while not user_in == 'buy':
    user_in = user_in.split()
    product = user_in[0]
    price = float(user_in[1])
    quantity = int(user_in[2])
    if product not in dict_product:
        dict_product[product] = [0.0, 0]
    dict_product[product][0] = price
    dict_product[product][1] += quantity

    user_in = input()

for product, values in dict_product.items():
    print(f'{product} -> {values[0] * values[1]:.2f}')
