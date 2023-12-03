import sys
import re

# valid_games = {
#     "red":12,
#     "green":13,
#     "blue":14
# }

def create_game_dict(game):
    invalid = 0
    bags_set = []
    color_pairs = []
    game=game[4:]
    key,values_str = game.split(":")
    key = int(key)
    sets = values_str.split(";")
    # Remove leading/trailing spaces
    for i,set in enumerate(sets):
        sets[i] = set.strip()
        bags_set.append(set.split(","))
    
    for i, bags in enumerate(bags_set):
        for i, color in enumerate(bags):
            bags[i] = color.strip()
            color_pairs.append(bags[i].split(" "))
    for i, color in enumerate(color_pairs):
        if color[1] == "red":
            if int(color[0]) > 12:
                invalid = invalid + 1
        if color[1] == "green":
            if int(color[0]) > 13:
                invalid = invalid + 1
        if color[1] == "blue":
            if int(color[0]) > 14:
                invalid = invalid + 1
    if invalid == 0:
        return key
    else:
        return 0




with open(sys.argv[1], 'r') as file:
    games = []
    for game in file:
        games.append(game)
sum = 0
for game in games:
    game_number = create_game_dict(game)
    sum = sum + game_number
print(sum)