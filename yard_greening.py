green_area = float(input())
total_before_discount = green_area * 7.61
discount = total_before_discount * 0.18
total = total_before_discount - discount

print(f"The final price is: {total} lv.")
print(f"The discount is: {discount} lv.")
