#!/usr/bin/python3

import sys
import re
from time import perf_counter_ns

_day = 8 #Advent of Code day

## BEGIN SOLUTION

def main(data):

    # Read Input
    cave_pat = re.compile(r"\w\w\w")
    caves = {}
    turns = data[0][:-1]

    for line in data[2:]:
        cave = cave_pat.findall(line)
        caves[cave[0]] = (cave[1], cave[2])

    # Run Caves
    steps = 0
    here = "AAA"
    step = 0

    while here != "ZZZ":
        turn = turns[step]

        if turn == 'L':
            here = caves[here][0]
        elif turn == 'R':
            here = caves[here][1]
        else:
            raise ValueError(f"You just walked into a wall: {turn}")

        step = (step+1) % len(turns)
        steps += 1

    print(f"It took {steps} steps to leave the cave")

    
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

