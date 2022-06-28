from math import floor
book_pages = int(input())
pages_per_hour = int(input())
days= int(input())
total_time = book_pages // pages_per_hour
hours_to_read =  total_time // days
print(hours_to_read)
