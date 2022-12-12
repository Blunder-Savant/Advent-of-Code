#!/usr/bin/env python3

from pathlib import Path

def BFS(height_map, start_coord, end_coord):
    fringe = list()
    fringe.append({"coord": start_coord, "steps": 0})

    visited = set()

    while fringe:
        square = fringe.pop(0)

        if square["coord"] == end_coord:
            return square["steps"]

        if square["coord"] in visited: 
            continue

        visited.add(square["coord"])
        row, col = square["coord"]

        moves = [
            coord
            for coord in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
            if 0 <= coord[0] < len(height_map)
            and 0 <= coord[1] < len(height_map[0])
            and height_map[coord[0]][coord[1]] - height_map[row][col] <= 1
        ]

        for move in moves:
            fringe.append({"coord": move, "steps": square["steps"] + 1})

    return float("inf")  # Failed to find path


height_map = list()

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    for line in file.read().split():
        height_map.append([ord(chr) for chr in line])  # Convert each char to ASCII value

for row in range(len(height_map)):
    for col in range(len(height_map[0])):

        if height_map[row][col] == ord("S"):  # Start coordinate
            start = (row, col)
            height_map[row][col] = ord("a")

        if height_map[row][col] == ord("E"):  # End coordinate
            end = (row, col)
            height_map[row][col] = ord("z")

print(BFS(height_map, start, end))