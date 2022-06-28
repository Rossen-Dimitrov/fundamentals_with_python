steps = 0

while steps < 10000:
    user_input = input()
    if user_input == "Going home":
        steps_home = int(input())
        steps += steps_home
        break
    steps += int(user_input)

if steps >= 10000:
    print("Goal reached! Good job!")
    print(f"{steps- 10000} steps over the goal!")
else:
    print(f"{10000 - steps} more steps to reach goal.")