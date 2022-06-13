initial_energy = 100
initial_coins = 100
day_events = input().split('|')
condition = False

for event in day_events:
    work_event = event.split('-')
    event_ingredient = work_event[0]
    number = int(work_event[1])
    if event_ingredient == 'rest':
        if initial_energy + number <= 100:
            initial_energy += number
            print(f"You gained {number} energy.")
        else:
            temp_gain = 100 - initial_energy
            initial_energy = 100
            print(f"You gained {temp_gain} energy.")
        print(f"Current energy: {initial_energy}.")
    elif event_ingredient == 'order':
        if initial_energy >= 30:
            initial_energy -= 30
            initial_coins += number
            print(f'You earned {number} coins.')
        else:
            initial_energy += 50
            if initial_energy > 100:
                initial_energy = 100
            print("You had to rest!")
    else:
        if initial_coins >= number:
            initial_coins -= number
            print(f"You bought {event_ingredient}.")
        else:
            condition = True
            print(f"Closed! Cannot afford {event_ingredient}.")
            break

if not condition:
    print(f"Day completed!\nCoins: {initial_coins}\nEnergy: {initial_energy}")
