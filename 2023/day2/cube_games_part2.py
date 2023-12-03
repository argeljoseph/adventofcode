import sys
import re

# valid_games = {
#     "red":12,
#     "green":13,
#     "blue":14
# }

def create_game_dict(game):
    invalid = 0
    red_color = []
    green_color = []
    blue_color = []
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
            red_color.append(int(color[0]))
        if color[1] == "green":
            green_color.append(int(color[0]))
        if color[1] == "blue":
            blue_color.append(int(color[0]))
    red_color.sort()
    green_color.sort()
    blue_color.sort()
    return red_color[-1] * green_color[-1] * blue_color[-1]

with open(sys.argv[1], 'r') as file:
    games = []
    for game in file:
        games.append(game)

sum = 0
for game in games:
    game_number = create_game_dict(game)
    sum = sum + game_number
print(sum)
