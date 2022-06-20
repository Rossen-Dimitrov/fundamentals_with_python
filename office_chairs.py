rooms = int(input())
total_free_chairs = 0
enough_chairs = True
for room in range(1, rooms + 1):
    command = input().split()
    chairs = command[0]
    visitors = int(command[1])
    total_free_chairs += len(chairs) - visitors
    if visitors > len(chairs):
        print(f"{visitors - len(chairs)} more chairs needed in room {room}")
        enough_chairs = False

if enough_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")
