import sys
list_of_integers = list(map(int, (input().split())))
commands = input()
while not commands == 'end':
    split_commands = commands.split()
    manipulator = split_commands[0]
    sec_param = split_commands[1]
    if manipulator == "exchange":
        if 0 <= int(sec_param) <= len(list_of_integers):
            list_of_integers = list_of_integers[int(sec_param) + 1:] + list_of_integers[:int(sec_param) + 1]
        else:
            print("Invalid index")
    elif manipulator == "max":
        if sec_param == 'even':
            num = -sys.maxsize
            index = 0
            for cur_index, cur_num in enumerate(list_of_integers):
                if cur_num % 2 == 0:
                    if cur_num >= num:
                        num = cur_num
                        index = cur_index
            if num == -sys.maxsize:
                print("No matches")
            else:
                print(index)
        elif sec_param == 'odd':
            num = -sys.maxsize
            index = 0
            for cur_index, cur_num in enumerate(list_of_integers):
                if not cur_num % 2 == 0:
                    if cur_num >= num:
                        num = cur_num
                        index = cur_index
            if num == -sys.maxsize:
                print("No matches")
            else:
                print(index)
    elif manipulator == "min":
        if sec_param == 'even':
            num = sys.maxsize
            index = 0
            for cur_index, cur_num in enumerate(list_of_integers):
                if cur_num % 2 == 0:
                    if cur_num <= num:
                        num = cur_num
                        index = cur_index
            if num == sys.maxsize:
                print("No matches")
            else:
                print(index)
        elif sec_param == 'odd':
            num = sys.maxsize
            index = 0
            for cur_index, cur_num in enumerate(list_of_integers):
                if not cur_num % 2 == 0:
                    if cur_num <= num:
                        num = cur_num
                        index = cur_index
            if num == sys.maxsize:
                print("No matches")
            else:
                print(index)
    elif manipulator == "first":
        if int(sec_param) > len(list_of_integers):
            print("Invalid count")
        else:
            even_or_odd = split_commands[2]
            even_nums = []
            odd_nums = []
            for num in list_of_integers:
                if num % 2 == 0:
                    even_nums.append(num)
                else:
                    odd_nums.append(num)
            if even_or_odd == 'even':
                print(even_nums[:int(sec_param)])
            else:
                print(odd_nums[:int(sec_param)])
    elif manipulator == "last":
        if int(sec_param) > len(list_of_integers):
            print("Invalid count")
        else:
            even_or_odd = split_commands[2]
            even_nums = []
            odd_nums = []
            for num in list_of_integers:
                if num % 2 == 0:
                    even_nums.append(num)
                else:
                    odd_nums.append(num)
            if even_or_odd == 'even':
                print(even_nums[-int(sec_param):])
            else:
                print(odd_nums[-int(sec_param):])

    commands = input()
print(list_of_integers)
