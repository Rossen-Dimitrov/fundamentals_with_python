pens = int(input())
markers = int(input())
cleaning = int(input())
discount = int(input()) / 100

pens_price = pens * 5.8
markers_price = markers * 7.2
cleaning_price = cleaning * 1.2
total = (pens_price + markers_price + cleaning_price)
total_with_discount = total - (total * discount)
print(total_with_discount)