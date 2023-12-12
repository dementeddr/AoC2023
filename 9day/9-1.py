#!/usr/bin/python3

import sys
import re
from time import perf_counter_ns

_day = 9 #Advent of Code day

## BEGIN SOLUTION

def main(data):

    end_totals = 0

    for line in data:
        readings = list(map(int, line.split()))
        next_num = diff_row(readings)
        print(next_num)
        end_totals += next_num

    print(f"\nSum of predicted readings is {end_totals}")


def diff_row(row):

    next_row = []
    is_zeros = True

    for i in range(len(row)-1):
        num = row[i+1] - row[i]
        next_row.append(num)
        if num != 0:
            is_zeros = False

    if is_zeros:
        print(f"  Bottom: {row[-1]} + 0")
        return row[-1]

    end = diff_row(next_row)
    print(f" {end} + {row[-1]} = {end+row[-1]}")
    return row[-1] + end

    
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

