#!/usr/bin/env python3

from pathlib import Path

p = Path(__file__).with_name("input.txt")
with p.open("r") as file:
    terminal = file.read().split("$ ")

root = ""
file_system = {root: list()}

for line in terminal[1:]:
    cmd = line.split()[0]
    out = line.split()[1:]

    if cmd == "cd":

        # move to outermost directory
        if out[0] == "/":
            path = root

        # move out one level
        elif out[0] == "..":
            path = path[:path.rfind("/")]

        # move in one level [dir]
        else:
            path = path + "/" + out[0]

    if cmd == "ls":
        for i in range(0, len(out), 2):
            
            # out = [dir] [name]
            if out[i] == "dir":
                new_dir = path + "/" + out[i+1]
                if new_dir not in file_system:
                    file_system[new_dir] = list()

            # out = [size] [file]
            else:
                file_system[path].append(int(out[i]))
                    

dir_bytes = dict()  # Store total number of bytes for each directory (including child directories) 

for path in file_system:
    file_sizes = sum(file_system[path])

    while True:
        if path not in dir_bytes:
            dir_bytes[path] = file_sizes
        else:
            dir_bytes[path] += file_sizes

        if path == "":
            break

        path = path[:path.rfind("/")]   
        
unused_space = 70000000 - dir_bytes[root]
free_up_space = 30000000 - unused_space

print(min(size for size in dir_bytes.values() if size >= free_up_space))