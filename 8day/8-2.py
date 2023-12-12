#!/usr/bin/python3

import sys
import re
from time import perf_counter_ns
from functools import reduce

_day = 8 #Advent of Code day

## BEGIN SOLUTION

def main(data):

    # Read Input
    cave_pat = re.compile(r"\w\w\w")
    caves = {}
    turns = data[0][:-1]
    starts = []

    for line in data[2:]:
        cave = cave_pat.findall(line)
        caves[cave[0]] = (cave[1], cave[2])
        if cave[0][-1] == 'A':
            starts.append(cave[0])

    # Run Caves
    print(f"Starts: {starts}")
    print(f"Turns: (len {len(turns)}) {turns}")

    zsteps = list(map(lambda s: walk_nodes(s, turns, caves), starts))
    print(zsteps)

    steps = reduce(lambda x, y: (x * y) // len(turns), zsteps)
    print(f"\nIt took {steps} quantum steps to leave the cave")
    

def walk_nodes(start, turns, caves):
    node = start
    zsteps = {}
    whole_set = []
    turn = 0
    step = 0

    while True:
        step += 1

        if turns[turn] == 'L':
            node = caves[node][0]
        elif turns[turn] == 'R':
            node = caves[node][1]
        else:
            raise ValueError(f"You just walked into a wall: {turn}")

        if node[-1] == 'Z':
            #print(f"  Step {step+1}: turns[{turn}] = {turns[turn]}, node = '{node}'")
            #print(f"    Adding '{node}' to zsteps")
            return step

        turn = (turn + 1) % len(turns)



## END SOLUTION

if __name__ == "__main__":
    input_file = f"input-d{_day}.txt"
    data = []

    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    with open(input_file, "r") as fp:
        data = fp.readlines()

    time_start = perf_counter_ns()
    main(data)
    time_stop = perf_counter_ns()

    time = (time_stop - time_start) / 1000000
    print(f"\nExecution took {time:.4f} milliseconds")

