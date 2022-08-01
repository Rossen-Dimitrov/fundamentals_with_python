import re
runners_dict = dict.fromkeys(input().split(', '), 0)


line_in = input()
while not line_in == "end of race":
    runner = "".join(re.findall(r"[a-z]|[A-Z]", line_in))
    digit_list = re.findall(r"\d", line_in)
    distance = 0
    for x in digit_list:
        distance += int(x)
    if runner in runners_dict:
        runners_dict[runner] += distance
    line_in = input()

runners_sorted = {k: v for k, v in sorted(runners_dict.items(), key=lambda v: v[1], reverse=True)}
winners = []
for name in runners_sorted.keys():
    winners.append(name)

print(f'1st place: {winners[0]}')
print(f'2nd place: {winners[1]}')
print(f'3rd place: {winners[2]}')
