easter_bred = int(input())
sugar_used = 0
flour_used = 0
max_used_flour = 0
max_used_sugar = 0
needed_flour = 0
needed_sugar = 0
for n in range(easter_bred):
    sugar_input = int(input())
    flour_input = int(input())
    sugar_used += sugar_input
    flour_used += flour_input
    if sugar_input > max_used_sugar:
        max_used_sugar = sugar_input
    if flour_input > max_used_flour:
        max_used_flour = flour_input
while sugar_used > 950:
    needed_sugar += 1
    sugar_used -= 950
    if sugar_used <= 950:
        needed_sugar += 1
        break
while flour_used > 750:
    needed_flour += 1
    flour_used -= 750
    if flour_used <= 750:
        needed_flour += 1
        break
print(f"Sugar: {needed_sugar}")
print(f"Flour: {needed_flour}")
print(f"Max used flour is {max_used_flour} grams, max used sugar is {max_used_sugar} grams.")
