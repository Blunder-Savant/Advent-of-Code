#!/usr/bin/env python3

from pathlib import Path

GROVE_COORDS = (1000, 2000, 3000)
DECRYPTION_KEY = 811589153
MIXING_COUNT = 10

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    encrypted_file = [int(num) for num in file.read().split()]

# Apply decryption key
decypted_file = [num * DECRYPTION_KEY for num in encrypted_file]

# Couple decypted value with encrypted value index
decypted_file = list(zip(decypted_file, range(len(encrypted_file))))

for round in range(MIXING_COUNT):
    for ei in range(len(encrypted_file)):
        di = [i for num, i in decypted_file].index(ei)
    
        num = decypted_file.pop(di)[0]
        new_di = (di + num) % len(decypted_file)
        decypted_file.insert(new_di, (num, ei))

# Shift file such that its zero value is the first element
zero_index = [num for num, i in decypted_file].index(0)
decypted_file = decypted_file[zero_index:] + decypted_file[:zero_index] 

print(sum(decypted_file[coord % len(decypted_file)][0] for coord in GROVE_COORDS))