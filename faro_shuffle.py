cards_list = input().split()
shuffles = int(input())

for mix in range(shuffles):
    deck_a = cards_list[:len(cards_list) // 2]
    deck_b = cards_list[len(cards_list) // 2:]
    cards_list.clear()
    for index in range(len(deck_a)):
        cards_list.append(deck_a[index])
        cards_list.append(deck_b[index])
print(cards_list)
