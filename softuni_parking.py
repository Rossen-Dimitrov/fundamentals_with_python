n_users = int(input())

parking = {}

for cars in range(n_users):
    input_command = input().split()
    command = input_command[0]
    user = input_command[1]
    if command == 'register':
        plate_num = input_command[2]
        if user in parking.keys():
            print(f"ERROR: already registered with plate number {plate_num}")
        else:
            print(f"{user} registered {plate_num} successfully")
            parking[user] = plate_num
    elif command == 'unregister':
        if user in parking:
            print(f"{user} unregistered successfully")
            del parking[user]
        else:
            print(f"ERROR: user {user} not found")

for user, plate_num in parking.items():
    print(f"{user} => {plate_num}")
