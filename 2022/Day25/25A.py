#!/usr/bin/env python3

from pathlib import Path

snafu_digits = {
    "2": 2,
    "1": 1,
    "0": 0,
    "-": -1,
    "=": -2 
}

def snafu_to_decimal(snafu):
    place = 1
    num = 0

    for digit in reversed(snafu):
        num += snafu_digits[digit] * place
        place *= 5
    
    return num


def decimal_to_snafu(num):
    place = 1
    snafu = str()

    # Find total number of snafu places
    while not (place * -2.5 < num < place * 2.5):
        place *= 5
    
    # Calculate each snafu digit, starting with the most significant digit
    while place != 0:

        upper_bound = place + place//2
        lower_bound = place - place//2

        if num > upper_bound:
            snafu += "2"
            num -= snafu_digits["2"] * place

        elif lower_bound <= num <= upper_bound:
            snafu += "1"
            num -= snafu_digits["1"] * place

        elif num < -upper_bound:
            snafu += "="
            num -= snafu_digits["="] * place

        elif -upper_bound <= num <= -lower_bound:
            snafu += "-"
            num -= snafu_digits["-"] * place

        else:
            snafu += "0"

        place //= 5

    return snafu


p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    snafu_list = file.read().split()

decimal_list = [snafu_to_decimal(snafu) for snafu in snafu_list]
total_num = sum(decimal_list)

# Test snafu <-> decimal conversion
assert snafu_list == [decimal_to_snafu(snafu_to_decimal(snafu)) for snafu in snafu_list]

print(decimal_to_snafu(total_num))