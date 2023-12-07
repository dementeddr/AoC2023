#!/usr/bin/python3

import sys
import re
from time import perf_counter_ns

_day = 6 #Advent of Code day

## BEGIN SOLUTION

def main(data):

    num_pat = re.compile(r"(\d+)")
    times = list(map(int,num_pat.findall(data[0])))
    dists = list(map(int,num_pat.findall(data[1])))
    print(times)
    print(dists)

    beats = 1
    for race in range(len(times)):
        print(f"{race}: time = {times[race]}, dist = {dists[race]}")
        rng = 0
        for i in range(times[race]):
            travel = i * (times[race] - i)
            if travel > dists[race]:
                rng += 1
            print(f"  [{i}]: travel = {travel}, range = {rng}")
        beats *= rng

    print(f"Margin = {beats}")



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

