last_sector = str(input())
first_sector_rows = int(input())
places_odd_raw = int(input())
total = 0
for sector in range(ord("A"), ord(last_sector) + 1):
    first_sector_rows += 1
    for rows in range(1, first_sector_rows):
        if rows % 2 == 0:
            for odd_even in range(ord("a"), ord("a") + places_odd_raw + 2):
                print(f"{chr(sector)}{rows}{chr(odd_even)}")
                total += 1
        else:
            for odd_raw in range(ord("a"), ord("a") + places_odd_raw):
                print(f"{chr(sector)}{rows}{chr(odd_raw)}")
                total += 1
print(total)
