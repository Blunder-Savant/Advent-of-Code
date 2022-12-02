#!/usr/bin/env python3

from pathlib import Path

shape_scores = {
    "A": 1,  # Rock
    "B": 2,  # Paper
    "C": 3,  # Scissors

    "X": 1,  # Rock
    "Y": 2,  # Paper
    "Z": 3   # Scissors
}

round_scores = {
    "lost": 0,
    "draw": 3,
    "won": 6
}

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    total_score = 0

    for line in file:
        opponent_move, my_move = line.split()

        total_score += shape_scores[my_move]

        if shape_scores[my_move] - shape_scores[opponent_move] in {1, -2}:
            total_score += round_scores["won"]
        elif shape_scores[my_move] == shape_scores[opponent_move]:
            total_score += round_scores["draw"]
        else:
            total_score += round_scores["lost"]
        
print(total_score)