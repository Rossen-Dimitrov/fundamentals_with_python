def data_type(value_type, value):
    if value_type == "int":
        print(int(value) * 2)
    elif value_type == "real":
        print(f'{float(value) * 1.5:.2f}')
    elif value_type == "string":
        print(f"${value}$")


data_type(input(), input())
