#!/usr/bin/env python3
from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    almanac = file.read().split("\n\n")

seed_ranges = [int(seed) for seed in almanac[0].split()[1:]]
seed_generators = [range(seed_num, seed_num + seed_len) for seed_num, seed_len in list(zip(seed_ranges, seed_ranges[1:]))[::2]]

master_map = dict()
location_nums = list()

for map in almanac[1:]:
    src_id = map.split()[0].split("-")[0]
    dst_id = map.split()[0].split("-")[2]
    ranges = [[int(num) for num in line.split()] for line in map.split("\n")[1:]]

    master_map[src_id] = [dst_id, ranges]

for seed_range in seed_generators:
    for seed in seed_range:
        num = seed
        map_id = "seed"

        while (map_id != "location"):
            next_map_id = master_map[map_id][0]
    
            for dst, src, src_len in master_map[map_id][1]:
                if num >= src and num < src + src_len:
                    num = dst + (num - src)
                    break
        
            map_id = next_map_id
        
        location_nums.append(num)

print(min(location_nums))
