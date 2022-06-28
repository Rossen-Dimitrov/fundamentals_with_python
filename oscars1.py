actor_name = input()
points = float(input())
judges = int(input())

for _ in range(judges):
    judge_name = input()
    judge_point = float(input())
    points += (len(judge_name) * judge_point) / 2
    if points >= 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!")
        exit()
else:
    print(f"Sorry, {actor_name} you need {1250.5 - points:.1f} more!")