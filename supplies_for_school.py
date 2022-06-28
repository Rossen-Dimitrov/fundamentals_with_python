packets_of_pens = int(input('Пакети химикали: '))
packets_of_markers = int(input('Пакети маркери: '))
cleaning = int(input('Почистващ препарат: '))
discount = int(input('Отстъпка: '))
pens_prise = 5.8
markers_prise = 7.2
cleaning_prise = 1.2
discount /= 100
total_sum = packets_of_pens * pens_prise + packets_of_markers * markers_prise + cleaning_prise * cleaning
total_sum_discount = total_sum - (total_sum * discount)
print(total_sum_discount)