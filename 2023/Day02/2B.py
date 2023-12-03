#!/usr/bin/env python3
from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    games = file.read().split("\n")

power_games = list()

for game in games:
    _, game_sets = game.split(":")
    cubes = game_sets.replace(";", ",").split(",")

    r_max = max(int(cube[1:-4]) for cube in cubes if cube.endswith("red"))
    g_max = max(int(cube[1:-6]) for cube in cubes if cube.endswith("green"))
    b_max = max(int(cube[1:-5]) for cube in cubes if cube.endswith("blue"))

    power_games.append(r_max * g_max * b_max)

print(sum(power_games))
