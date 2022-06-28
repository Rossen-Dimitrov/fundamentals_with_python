from math import floor
pages = int(input())
page_p_hour = int(input())
days_p_book = int(input())
pages_p_book = pages / page_p_hour
days_p_book = pages_p_book / days_p_book
print(floor(days_p_book))
