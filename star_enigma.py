import re

n = int(input())

count_pattern = r"[STARstar]"
message_pattern = r"\@(?P<planet>[A-Za-z]+)[^@:!\->]*:(?P<population>\d+)" \
                  r"[^@:!\->]*!(?P<attack>[A|D])![^@:!\->]*\->(?P<soldier>\d+)"
attacked = []
destroyed = []

for i in range(n):
    temp_messages = ''
    data_in = input()
    count = len(re.findall(count_pattern, data_in))
    for char in data_in:
        temp_messages += (chr(ord(char) - count))
    message = re.search(message_pattern, temp_messages)
    if message:
        planet = message.group('planet')
        attack = message.group('attack')
        if attack == 'A':
            attacked.append(planet)
        else:
            destroyed.append(planet)

print(f'Attacked planets: {len(attacked)}')
if attacked:
    attacked = sorted(attacked)
    for planet in attacked:
        print(f"-> {planet}")

print(f'Destroyed planets: {len(destroyed)}')

if destroyed:
    destroyed = sorted(destroyed)
    for planet in destroyed:
        print(f"-> {planet}")
