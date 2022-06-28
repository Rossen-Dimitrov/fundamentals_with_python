goal = 10000
steps_counter = 0
condition = True
while True:
    user_input = input()
    if str(user_input) == "Going home":
        going_home_steps = int(input())
        steps_counter += going_home_steps
        if steps_counter >= goal:
            break
        else:
            condition = False
            break
    steps_counter += int(user_input)
    if steps_counter >= goal:
        break
if condition:
    print("Goal reached! Good job!")
    print(f"{steps_counter - goal} steps over the goal!")
else:
    print(f"{goal - steps_counter} more steps to reach goal.")
