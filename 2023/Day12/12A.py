#!/usr/bin/env python3
from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    spring_records = file.read().split("\n")


def find_patterns(line, i):
    if i == len(line):
        return [line]
    
    if line[i] == "?":
        patterns_with_dot =  find_patterns(line[:i] + "." + line[i + 1:], i + 1)
        patterns_with_hash = find_patterns(line[:i] + "#" + line[i + 1:], i + 1)
        return patterns_with_dot + patterns_with_hash

    return find_patterns(line, i + 1)


valid = {spring_record: list() for spring_record in spring_records}

for spring_record in spring_records:
    line, pattern = spring_record.split()
    pattern = [int(num) for num in pattern.split(",")]

    possible = find_patterns(line, 0)

    for line in possible:
        split_hashes = [hashes for hashes in line.split('.') if hashes]

        if len(pattern) != len(split_hashes):
            continue
        
        if all(len(split_hashes[i]) == num for i, num in enumerate(pattern)):
            valid[spring_record].append(line)

print(sum(len(lines) for lines in valid.values()))     
