#!/usr/bin/env python3

from pathlib import Path

RIGHT, DOWN, LEFT, UP = 0, 1, 2, 3

dirs = [RIGHT, DOWN, LEFT, UP]
tiles = dict()
moves = list()

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    board, guide = file.read().split("\n\n")

    # Parse board layout
    for row, line in enumerate(board.split("\n")):
        for col, tile in enumerate(line):
            if tile == "." or tile == "#":
                tiles[(row+1, col+1)] = tile

    # Parse guide instructions
    prev_i = 0
    for i, val in enumerate(guide.split()[0]):
        if val.isalpha():
            moves.append(int(guide[prev_i:i]))
            prev_i = i+1
            moves.append(val)

    if val.isdigit():
        moves.append(int(guide[prev_i:-1]))

# Starting conditions
pos = min(tile for tile in tiles if tile[0] == 1)
facing = RIGHT

while moves:
    move = moves.pop(0)

    # Move forward in facing direction
    if type(move) == int:
        if facing == LEFT or facing == RIGHT:
            tile_list = [tile for tile in tiles if tile[0] == pos[0]]
        else:
            tile_list = [tile for tile in tiles if tile[1] == pos[1]]

        for step in range(move):
            tile_index = tile_list.index(pos)

            if facing == DOWN or facing == RIGHT:
                next_tile = tile_list[(tile_index + 1) % len(tile_list)]
            else:
                next_tile = tile_list[(tile_index - 1) % len(tile_list)]

            if tiles[next_tile] == ".":
                pos = next_tile
            else:
                break
    
    # Rotate clockwise or counterclockwise
    elif type(move) == str:
        turn = -1 if move == "L" else 1
        facing = dirs[(facing + turn) % len(dirs)]

final_password = pos[0] * 1000 + pos[1] * 4 + facing
print(final_password)