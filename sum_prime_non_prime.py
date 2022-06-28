prime_num_sum = 0
non_prime_num_sum = 0
command = input()
while command != "stop":
    current_num = int(command)
    if current_num < 0:
        print("Number is negative.")
    else:
        number_is_prime = True
        for num in range(2, current_num):
            if current_num % num == 0:
                number_is_prime = False
                break
        if number_is_prime:
            prime_num_sum += current_num
        else:
            non_prime_num_sum += current_num
    command = input()
print(f"Sum of all prime numbers is: {prime_num_sum}")
print(f"Sum of all non prime numbers is: {non_prime_num_sum}")

