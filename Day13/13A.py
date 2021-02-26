#!/usr/bin/env python3

# Read input from file
with open("puzzle_input.txt") as file:
    input = file.readlines()

timestamp = int(input[0])
active_buses = set()

# Generate list of bus IDs that are in service according to the shuttle company
for bus in input[1].split(","):
    if bus != "x":
        active_buses.add(int(bus))


check_timestamp = timestamp
found_bus = None
found_timestamp = None

while found_bus == None:
    # Check when each bus will depart relative to the current timestamp
    for bus in active_buses:
        if check_timestamp % bus == 0:
            found_bus = bus
            found_timestamp = check_timestamp
            break

    check_timestamp += 1


time_wait = found_timestamp - timestamp
print(time_wait * bus)