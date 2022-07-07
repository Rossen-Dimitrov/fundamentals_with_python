data_in = input().split(' ')
searched = input().split()
bakery_dict = {data_in[i]: int(data_in[i + 1]) for i in range(0, len(data_in), 2)}

for product in searched:
    if product in bakery_dict:
        print(f"We have {bakery_dict.get(product)} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
