year = int(input()) + 1

for i in range(0, len(str(year))):
    cheker = str(year).count(str(year)[i])

    while cheker > 1:
        year += 1
        cheker = str(year).count(str(year)[i])

print(year)

# year = int(input())
# while True:
#     year += 1
#     current_year = str(year)
#     if len(set(current_year)) == len(current_year):
#         print(current_year)
#         break
