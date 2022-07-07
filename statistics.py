key_value_input = input()
products = {}
while not key_value_input == 'statistics':
    key_value_input = key_value_input.split(": ")
    key = key_value_input[0]
    value = int(key_value_input[1])
    if key not in products:
        products[key] = 0
    products[key] += value

    key_value_input = input()

print("Products in stock:")
for key, value in products.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
