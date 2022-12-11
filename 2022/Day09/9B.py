#!/usr/bin/env python3

from pathlib import Path

s = (0,0)
knots_prev_pos = {knot: s for knot in range(10)}
t_positions = {s}

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    for line in file:
        dir, steps = line.split()

        for step in range(int(steps)):

            h_row, h_col = knots_prev_pos[0]

            if dir == "U": h_row += 1
            if dir == "D": h_row -= 1
            if dir == "R": h_col += 1
            if dir == "L": h_col -= 1

            knots_prev_pos[0] = (h_row, h_col)

            for index in range(1, len(knots_prev_pos)):
                h_row, h_col = knots_prev_pos[index-1]
                t_row, t_col = knots_prev_pos[index]

                dy_row = h_row - t_row
                dx_col = h_col - t_col

                if abs(dy_row) > 1 or abs(dx_col) > 1:
    
                    if abs(dy_row) > 1 and h_col == t_col:
                        dy = 1 if dy_row > 0 else -1
                        t_row += dy
    
                    elif abs(dx_col) > 1 and h_row == t_row:
                        dx = 1 if dx_col > 0 else -1
                        t_col += dx
    
                    else:
                        dy = 1 if dy_row > 0 else -1
                        dx = 1 if dx_col > 0 else -1
                        t_row += dy
                        t_col += dx
                        
                    knots_prev_pos[index] = (t_row, t_col)

                    if index == 9:
                        t_positions.add((t_row, t_col))
    
print(len(t_positions))