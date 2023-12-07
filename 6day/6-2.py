#!/usr/bin/python3

import sys
import re
from time import perf_counter_ns

_day = 6 #Advent of Code day

## BEGIN SOLUTION

def main(data):

    num_pat = re.compile(r"(\d+)")
    time = int("".join(num_pat.findall(data[0])))
    dist = int("".join(num_pat.findall(data[1])))
    print(time)
    print(dist)

    beats = 0
    for i in range(time):
        travel = i * (time - i)
        if travel > dist:
            beats += 1
        #print(f"  [{i}]: travel = {travel}, beats = {beats}")

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

