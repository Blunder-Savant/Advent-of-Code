#!/usr/bin/env python3

from pathlib import Path

monkeys = dict()

def find_monkey_yell(name):
    if len(monkeys[name].split()) == 1:
        return monkeys[name]

    yell1 = find_monkey_yell(monkeys[name][0:4])
    sign = monkeys[name].split()[1]
    yell2 = find_monkey_yell(monkeys[name][7:11])

    return eval(str(yell1) + sign + str(yell2))


p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    for line in file.readlines():
        key, value = line.split(": ")
        monkeys[key] = value[:-1]

print(int(find_monkey_yell("root")))