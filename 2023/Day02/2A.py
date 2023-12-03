#!/usr/bin/env python3
from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    games = file.read().split("\n")

RED_CUBES = 12
GREEN_CUBES = 13
BLUE_CUBES = 14

possible_games = list()

for game in games:
    game_id, game_sets = game.split(":")

    game_id = int(game_id[5:])
    cubes = game_sets.replace(";", ",").split(",")

    r_max = max(int(cube[1:-4]) for cube in cubes if cube.endswith("red"))
    g_max = max(int(cube[1:-6]) for cube in cubes if cube.endswith("green"))
    b_max = max(int(cube[1:-5]) for cube in cubes if cube.endswith("blue"))

    if r_max <= RED_CUBES and g_max <= GREEN_CUBES and b_max <= BLUE_CUBES:
        possible_games.append(game_id)

print(sum(possible_games))
