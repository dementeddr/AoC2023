#!/usr/bin/python3

import sys
import re
from time import perf_counter_ns

_day = 13 #Advent of Code day

## BEGIN SOLUTION

def main(data):

    field = []
    total_ref = 0

    for line in data:
        if len(line) > 1:
            field.append(line.strip())
            continue
        

        mirror = find_mirror(field)
        print(f"Mirror: {mirror}")
        print_field(field)
        if mirror <= 0:
            print("Pivoting...")
            field = pivot(field)
            mirror = find_mirror(field)
            print(f"Mirror: {mirror}")
            print_field(field)
        
        total_ref += mirror
        field = []

    print(f"\nTotal reflected area = {total_ref}")

            

def find_mirror(field):
    prev_line = ''
    for y, line in enumerate(field):
        if line == prev_line and check_mirror(field, y):
            return y
        else:
            prev_line = line

    return 0


def check_mirror(field, mirror):

    for y in range(mirror, len(field)):
        yp = mirror - y
        
        if yp < 0:
            return True

        if field[y] != field[yp]:
            return False

    return True



def pivot(field):
    new_field = []

    for x, char in enumerate(field[0]):
        new_line = []

        for y, line in enumerate(field):
            new_line.append(line[x])

        new_field.append(new_line)
        new_line = []

    return new_field


def print_field(field):

    for line in field:
        print(''.join(line))

    print()

    
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

