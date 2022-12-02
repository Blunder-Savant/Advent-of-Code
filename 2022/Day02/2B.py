#!/usr/bin/env python3

from pathlib import Path

shape_scores = {
    "A": 1,  # Rock
    "B": 2,  # Paper
    "C": 3,  # Scissors
}

round_scores = {
    "X": 0,  # Lose
    "Y": 3,  # Draw
    "Z": 6   # Win
}

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    total_score = 0

    for line in file:
        opponent_move, round_outcome = line.split()

        total_score += round_scores[round_outcome]

        if round_outcome == "X":  # Lose
            my_score = shape_scores[opponent_move] + 2 if opponent_move == "A" else shape_scores[opponent_move] - 1
            total_score += my_score
        elif round_outcome == "Z":  # Win
            my_score = shape_scores[opponent_move] - 2 if opponent_move == "C" else shape_scores[opponent_move] + 1
            total_score += my_score
        else:  # Draw
            total_score += shape_scores[opponent_move]
        
print(total_score)