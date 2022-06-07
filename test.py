game_list = list(input().split(" "))
game = {'A': {0, }, 'B': {0, }}
game_was_terminated = False
for player in game_list:
    key, value = player.split("-")
    game.update({key: add(value)})
print(game)
