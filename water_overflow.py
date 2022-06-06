pipe_num = int(input())
capacity = 255
for _ in range(pipe_num):
    litters_to_pour = int(input())
    if capacity - litters_to_pour > 0:
        capacity -= litters_to_pour
    else:
        print("Insufficient capacity!")

print(255 - capacity)
