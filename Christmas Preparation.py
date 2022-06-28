paper = int(input())
fabric = int(input())
glue = float(input())
discount = int(input())

paper_price = 5.80
fabric_price = 7.20
glue_price = 1.20

total = (paper * paper_price + fabric_price * fabric + glue_price * glue)
discount = total * discount / 100
total = total - discount
print(f"{total:.3f}")