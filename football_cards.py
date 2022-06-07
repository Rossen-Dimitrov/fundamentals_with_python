game_list = list(input().split(" "))
game = {'A': {0, }, 'B': {0, }}
game_was_terminated = False
for player in game_list:
    key, value = player.split("-")
    game.setdefault(key, set()).add(value)
    if len(game['A']) > 5 or len(game['B']) > 5:
        game_was_terminated = True
        break

print(f"Team A - {12 - len(game['A'])}; Team B - {12 - len(game['B'])}")
if game_was_terminated:
    print('Game was terminated')


# game_list = list(input().split(" "))
# team_a = set()
# team_b = set()
# game_was_terminated = False
# for player in game_list:
#     if player[0] == "A":
#         team_a.add(player)
#     elif player[0] == "B":
#         team_b.add(player)
#     if 11 - len(team_a) < 7 or 11 - len(team_b) < 7:
#         game_was_terminated = True
#         break
#
# print(f"Team A - {11 - len(team_a)}; Team B - {11 - len(team_b)}")
# if game_was_terminated:
#     print('Game was terminated')
