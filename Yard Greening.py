square_meters_for_landscaping = float(input())
price_for_the_hole_yard = square_meters_for_landscaping * 7.61
discount = price_for_the_hole_yard * 0.18
total_sum = price_for_the_hole_yard - discount
print(f"The final price is: {total_sum} lv.")
print(f"The discount is: {discount} lv.")