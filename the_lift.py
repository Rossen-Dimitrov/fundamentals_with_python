waiting = int(input())
current_state = input().split()
current_state_as_int = list(map(int, current_state))
slot = 0
condition = False
for places in current_state_as_int:
    if waiting + places >= 4:
        waiting -= 4 - places
        current_state_as_int[slot] += (4 - places)
        slot += 1
    else:
        current_state_as_int[slot] += waiting
        waiting = 0
        condition = True
current_state_as_str = list(map(str, current_state_as_int))
if condition:
    print("The lift has empty spots!")

elif waiting > 0:
    print(f"There isn't enough space! {waiting} people in a queue!")

print(' '.join(current_state_as_str))