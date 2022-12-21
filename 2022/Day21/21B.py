#!/usr/bin/env python3

from pathlib import Path

monkeys = dict()
ME = "humn"

def find_monkey_yell(name):
    if len(monkeys[name].split()) == 1:
        return monkeys[name]

    yell1 = find_monkey_yell(monkeys[name][0:4])
    sign = monkeys[name].split()[1]
    yell2 = find_monkey_yell(monkeys[name][7:11])

    return eval(str(yell1) + sign + str(yell2))

def am_i_relevant(name):
    if name == ME:
        return True

    if len(monkeys[name].split()) == 1:
        return False

    return am_i_relevant(monkeys[name][0:4]) or am_i_relevant(monkeys[name][7:11])


p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    for line in file.readlines():
        key, value = line.split(": ")
        monkeys[key] = value[:-1]

root_name1 = monkeys["root"][0:4]
root_name2 = monkeys["root"][7:11]

if am_i_relevant(root_name1):
    my_path = root_name1
    eq_path = root_name2
else:
    my_path = root_name2
    eq_path = root_name1

root_eq = find_monkey_yell(eq_path)

# Sample two values to determine linear relationship
sample = list()
for num in range(2):
    monkeys[ME] = str(num)
    sample.append(find_monkey_yell(my_path))

offset = sample[0]
slope = sample[1] - sample[0]

print(int((root_eq - offset) / slope))