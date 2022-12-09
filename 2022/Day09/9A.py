#!/usr/bin/env python3

from pathlib import Path

s = (0,0)
h_prev_pos = s
t_prev_pos = s
t_positions = {s}

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    for line in file:
        dir, num = line.split()
        num = int(num)

        for move in range(num):

            h_row, h_col = h_prev_pos
            t_row, t_col = t_prev_pos

            if dir == "U":
                h_row += 1
            if dir == "D":
                h_row -= 1
            if dir == "R":
                h_col += 1
            if dir == "L":
                h_col -= 1
    
            h_adj = [(i,j) for i in (h_row-1,h_row,h_row+1) for j in (h_col-1,h_col,h_col+1)]
    
            if t_prev_pos not in h_adj:
                if h_row != t_row and h_col != t_col:  # Check diagonal
                    if dir == "U" or dir == "D":
                        t_col = h_col
                    if dir == "R" or dir == "L":
                        t_row = h_row
                    
                if dir == "U":
                    t_row += 1
                if dir == "D":
                    t_row -= 1
                if dir == "R":
                    t_col += 1
                if dir == "L":
                    t_col -= 1
                
                t_positions.add((t_row, t_col))

            h_prev_pos = (h_row, h_col)
            t_prev_pos = (t_row, t_col)
    
print(len(t_positions))