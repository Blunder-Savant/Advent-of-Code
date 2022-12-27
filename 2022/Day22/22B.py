#!/usr/bin/env python3

from pathlib import Path

RIGHT, DOWN, LEFT, UP = 0, 1, 2, 3

dirs = [RIGHT, DOWN, LEFT, UP]
tiles = dict()
moves = list()

SIDE_LEN = 50

# Cube face layout (only 6 faces will populate)
#    00 01 02 03
#    10 11 12 13
#    20 21 22 23
#    30 31 32 33
cube_face_tiles = {str(row)+str(col): set() for row in range(4) for col in range(4)}

# Hard-coding each cube face to its wrapped cube face
CUBE_WRAP = {
    ("01", LEFT): ("20", RIGHT),
    ("20", LEFT): ("01", RIGHT),

    ("01", UP): ("30", RIGHT),
    ("30", LEFT): ("01", DOWN),

    ("02", RIGHT): ("21", LEFT),
    ("21", RIGHT): ("02", LEFT),

    ("02", DOWN): ("11", LEFT),
    ("11", RIGHT): ("02", UP),

    ("02", UP): ("30", UP),
    ("30", DOWN): ("02", DOWN),

    ("11", LEFT): ("20", DOWN),
    ("20", UP): ("11", RIGHT),

    ("21", DOWN): ("30", LEFT),
    ("30", RIGHT): ("21", UP)
}


def find_wrapped_position(pos, facing, new_facing):
    # Prepare and populate matrix 
    matrix = [[0 for col in range(SIDE_LEN)] for row in range(SIDE_LEN)]
    matrix[pos[0]][pos[1]] = 1

    # Rotate matrix counterclockwise
    while facing != dirs[(new_facing-2) % len(dirs)]:
        matrix = list(reversed(list(zip(*matrix))))
        facing = dirs[(facing-1) % len(dirs)]

    # Extract new position
    new_pos = [(row, col) for row in range(SIDE_LEN) for col in range(SIDE_LEN) if matrix[row][col] == 1].pop()

    # Flip new position vertically or horizontally
    if new_facing == UP or new_facing == DOWN:
        new_pos = (new_pos[0], SIDE_LEN-1 - new_pos[1])
    else:
        new_pos = (SIDE_LEN-1 - new_pos[0], new_pos[1])

    return new_pos


p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    board, guide = file.read().split("\n\n")

    # Parse board layout
    for row, line in enumerate(board.split("\n")):
        for col, tile in enumerate(line):
            if tile == "." or tile == "#":
                tiles[(row, col)] = tile

                # Put each coordinate into cube face lookup table
                cube_face_tiles[str(row//SIDE_LEN) + str(col//SIDE_LEN)].add((row, col))

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
pos = min(tile for tile in tiles if tile[0] == 0)
facing = RIGHT

while moves:
    move = moves.pop(0)

    # Move forward in facing direction
    if type(move) == int:
        new_facing = facing

        for step in range(move):
            if facing == RIGHT:
                next_tile = (pos[0], pos[1]+1)
            if facing == DOWN:
                next_tile = (pos[0]+1, pos[1])
            if facing == LEFT:
                next_tile = (pos[0], pos[1]-1)
            if facing == UP:
                next_tile = (pos[0]-1, pos[1])
    
            if next_tile not in tiles:
                # Get current and wrapped cube face
                face = str(pos[0]//SIDE_LEN) + str(pos[1]//SIDE_LEN)
                new_face, new_facing = CUBE_WRAP[(face, facing)]
    
                face_pos = (pos[0]%SIDE_LEN, pos[1]%SIDE_LEN)
                face_pos = find_wrapped_position(face_pos, facing, new_facing)
                next_tile = (face_pos[0] + int(new_face[0])*SIDE_LEN, face_pos[1] + int(new_face[1])*SIDE_LEN)
    
            if tiles[next_tile] == ".":
                pos = next_tile
                facing = new_facing
            else:
                break

    # Rotate clockwise or counterclockwise
    elif type(move) == str:
        turn = -1 if move == "L" else 1
        facing = dirs[(facing + turn) % len(dirs)]

final_password = (pos[0]+1) * 1000 + (pos[1]+1) * 4 + facing
print(final_password)