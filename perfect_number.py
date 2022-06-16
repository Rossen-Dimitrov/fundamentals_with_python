def perfect_number(number):
    condition = False
    for num in range(100):
        if number == (2 ** (num - 1)) * ((2 ** num) - 1):
            condition = True
            break
    if condition:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


perfect_number(int(input()))
