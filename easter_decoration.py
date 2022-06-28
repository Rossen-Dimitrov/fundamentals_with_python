customers = int(input())
total_sum = 0
for num_of_customers in range(customers):
    item_counter = 0
    total_current = 0
    while True:
        purchase = str(input())
        if purchase == "Finish":
            break
        else:
            item_counter += 1
            if purchase == "basket":
                total_current += 1.5
            elif purchase == "wreath":
                total_current += 3.8
            elif purchase == "chocolate bunny":
                total_current += 7
    if item_counter % 2 == 0:
        total_current *= 0.8
    total_sum += total_current
    print(f"You purchased {item_counter} items for {total_current:.2f} leva.")
print(f"Average bill per client is: {total_sum / customers:.2f} leva.")


