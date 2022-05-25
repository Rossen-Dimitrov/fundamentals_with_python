string_input = input().split(', ')
for index, animals in enumerate(string_input[::-1]):
    if animals == 'wolf' and index == 0:
        print("Please go away and stop eating my sheep")
    elif animals == 'wolf' and not index == 0:
        print(f"Oi! Sheep number {index}! You are about to be eaten by a wolf!")
