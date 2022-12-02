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

win_conditions = {
    "A": "C",  # Rock defeats Scissors
    "B": "A",  # Paper defeats Rock
    "C": "B",  # Scissors defeats Paper
}

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    total_score = 0

    for line in file:
        opponent_move, round_outcome = line.split()

        total_score += round_scores[round_outcome]

        if round_outcome == "X":  # Lose
            total_score += shape_scores[win_conditions[opponent_move]]
        elif round_outcome == "Z":  # Win
            total_score += shape_scores[win_conditions[win_conditions[opponent_move]]]
        else:  # Draw
            total_score += shape_scores[opponent_move]

print(total_score)