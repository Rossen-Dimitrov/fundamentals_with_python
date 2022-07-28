n = int(input())

my_heroes = {}

for i in range(n):
    cur_hero, hit_points, mana_points = input().split()
    my_heroes[cur_hero] = {'HP': int(hit_points), 'MP': int(mana_points)}

data_in = input()
while not data_in == "End":
    data_in = data_in.split(' - ')
    command, hero = data_in[0], data_in[1]

    if command == "CastSpell":
        mp_needed, spell = int(data_in[2]), data_in[3]
        if my_heroes[hero]["MP"] - mp_needed >= 0:
            my_heroes[hero]["MP"] -= mp_needed
            print(f"{hero} has successfully cast {spell} and now has {my_heroes[hero]['MP']} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell}!")

    elif command == "TakeDamage":
        damage, attacker = int(data_in[2]), data_in[3]
        if my_heroes[hero]['HP'] - damage > 0:
            my_heroes[hero]['HP'] -= damage
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {my_heroes[hero]['HP']} HP left!")
        else:
            print(f"{hero} has been killed by {attacker}!")
            del my_heroes[hero]

    elif command == "Recharge":
        amount = int(data_in[2])
        if my_heroes[hero]["MP"] + amount > 200:
            amount = 200 - my_heroes[hero]["MP"]
            print(f"{hero} recharged for {amount} MP!")
            my_heroes[hero]["MP"] = 200
        else:
            my_heroes[hero]["MP"] += amount
            print(f"{hero} recharged for {amount} MP!")

    elif command == "Heal":
        amount = int(data_in[2])
        if my_heroes[hero]["HP"] + amount > 100:
            amount = 100 - my_heroes[hero]["HP"]
            print(f"{hero} healed for {amount} HP!")
            my_heroes[hero]["HP"] = 100
        else:
            my_heroes[hero]["HP"] += amount
            print(f"{hero} healed for {amount} HP!")

    data_in = input()

for hero in my_heroes:
    print(hero)
    print(f"  HP: {my_heroes[hero]['HP']}")
    print(f"  MP: {my_heroes[hero]['MP']}")
