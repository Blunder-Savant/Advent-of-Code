#!/usr/bin/env python3

# Read input from file
with open("puzzle_input_ex.txt") as file:
    input = file.read()

grid = list()

# Generate 2D grid of each seat
for row in input.split("\n"):
    grid.append(list(row))


def check_neighbor(seat_row, seat_col):
    global grid
    occupied_seats = 0

    for adj_row in range(seat_row - 1, seat_row + 2):
        for adj_col in range(seat_col - 1, seat_col + 2):
            if adj_row == seat_row and adj_col == seat_col:
                continue
            if adj_row < 0 or adj_row > len(grid)-1:
                continue
            if adj_col < 0 or adj_col > len(grid[adj_row])-1:
                continue
            if grid[adj_row][adj_col] == "#":
                occupied_seats += 1

    return occupied_seats


change = 1

while(change > 0):

    change = 0
    new_grid = list()

    for row in range(len(grid)):
        temp = list()
        for col in range(len(grid[row])):
            adj_seats = check_neighbor(row, col)
            seat = grid[row][col]

            if seat == "L" and adj_seats == 0:
                temp.append("#")
                change += 1
            elif seat == "#" and adj_seats >= 5:
                temp.append("L")
                change += 1
            else:
                temp.append(seat)
        
        new_grid.append(temp)

    grid = new_grid.copy()


# Print grid
for line in grid:
    print(line)


# Count occupied seats
count = 0

for line in grid:
    for seat in line:
        if seat == "#":
            count += 1

print(count)