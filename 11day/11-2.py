#!/usr/bin/python3

import sys
import re
import math
from time import perf_counter_ns

_day = 11 #Advent of Code day

## BEGIN SOLUTION

def main(data):

    # Find expansion lines and galaxies

    blank_rows = []
    blank_cols = []
    galaxies = [] #(y, x) coordinate pairs

    for y in range(len(data)):
        if '#' not in data[y]:
            blank_rows.append(y)

    for x in range(len(data[0].strip())):
        found = False

        for y in range(len(data)):
            if data[y][x] == '#':
                galaxies.append( (y, x) )
                found = True

        if not found:
            blank_cols.append(x)

    print(f"Rows: {blank_rows}")
    print(f"Cols: {blank_cols}")
    print(f"Found {len(galaxies)} Galaxies")

    # Find all manhattan distances
    dist_total = 0

    for i in range(len(galaxies)-1):
        g1 = galaxies[i]

        for j in range(i+1,len(galaxies)):
            g2 = galaxies[j]
            dist_total += get_expanded_distance(g1, g2, blank_rows, blank_cols)

    print(f"\nIn the expanded universe, the total distance is {dist_total}")
            

def get_expanded_distance(g1, g2, blank_rows, blank_cols):

    #print(f"Galaxy pair: {g1} {g2}")
    
    x1 = min(g1[1], g2[1])
    x2 = max(g1[1], g2[1])
    y1 = min(g1[0], g2[0])
    y2 = max(g1[0], g2[0])

    dx = x2 - x1
    dy = y2 - y1

    expansion = 10**6 - 1

    #print(f"  before - dx: {dx}  dy: {dy}")

    for i in range(x1, x2):
        if i in blank_cols:
            dx += expansion

    for j in range(y1, y2):
        if j in blank_rows:
            dy += expansion
 
    #print(f"  after  - dx: {dx}  dy: {dy}")
    return dx + dy

    
    
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

