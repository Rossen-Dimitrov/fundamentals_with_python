first_num = int(input())
second_num = int(input())
third_num = int(input())
for num_1 in range(1, first_num + 1):
    if num_1 % 2 == 0:
        for num_2 in range(2, second_num + 1):
            if num_2 == 2 or num_2 == 3 or num_2 == 5 or num_2 == 7:
                for num_3 in range(1, third_num + 1):
                    if num_3 % 2 == 0:
                        print(f'{num_1} {num_2} {num_3}')