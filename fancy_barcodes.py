import re

n = int(input())
barcodes = []
valid_pattern = r"@#{1,}[A-Z][A-Za-z0-9]{4,}[A-Z]@#{1,}"
group_pattern = r""

for i in range(n):
    code = input()
    if re.findall(valid_pattern, code):
        number = ''
        for x in code:
            if x.isdigit():
                number += x
        if number:
            print(f"Product group: {number}")
        else:
            print(f"Product group: 00")
    else:
        print("Invalid barcode")

