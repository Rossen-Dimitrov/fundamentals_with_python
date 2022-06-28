from math import floor
total_book_pages = int(input())
pages_per_hour = int(input())
days_for_book = int(input())

hours_per_book = total_book_pages / pages_per_hour
days_to_read = hours_per_book / days_for_book
print(floor(days_to_read))