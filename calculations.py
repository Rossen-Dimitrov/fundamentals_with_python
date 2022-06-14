def calculator():
    parameter, num_a, num_b = str(input()), int(input()), int(input())
    result = None
    if parameter == "multiply":
        result = num_a * num_b
    elif parameter == "divide":
        result = int(num_a / num_b)
    elif parameter == "add":
        result = num_a + num_b
    elif parameter == "subtract":
        result = num_a - num_b
    return result


print(calculator())
