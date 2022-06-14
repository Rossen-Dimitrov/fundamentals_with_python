def calculator():
    parameter, num_a, num_b = str(input()), int(input()), int(input())
    if parameter == "multiply":
        return num_a * num_b
    elif parameter == "divide":
        return int(num_a / num_b)
    elif parameter == "add":
        return num_a + num_b
    elif parameter == "subtract":
        return num_a - num_b


print(calculator())
