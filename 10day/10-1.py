#!/usr/bin/python3

import sys
import re
from time import perf_counter_ns

_day = 10 #Advent of Code day

## BEGIN SOLUTION

offsets = { # (y, x)
    'L':[(-1, 0),( 0, 1)],
    'F':[( 1, 0),( 0, 1)],
    'J':[(-1, 0),( 0,-1)],
    '7':[( 1, 0),( 0,-1)],
    '-':[( 0,-1),( 0, 1)],
    '|':[(-1, 0),( 1, 0)]
    }

def main(data):

    S = (-1, -1)

    data = list(map(str.strip, data))

    print(f"Size: {len(data)} x {len(data[0])}")

    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == 'S':
                S = (y, x)
                print(f"S at {S}")
                break

        if S != (-1,-1):
            break

    starts = [(-1,0), (0,1), (1,0), (0,-1)]
    #dists = {}
    dist = 0

    for start in starts:
        prev_coord = S
        coord = add_coords(S, start)
        pipe = coord_get(coord, data)
        dist = 1

        print(f"Start at {coord} (offset {start})")
        
        while pipe != 'S':
            
            connectors = list(map(lambda c: add_coords(coord, c), offsets[pipe]))
            
            print(f"  Coord = {coord}. Pipe = {pipe}, dist = {dist}   conns = {connectors}")
            
            if prev_coord not in connectors:
                break

            connectors.remove(prev_coord)
            prev_coord = coord
            coord = connectors[0]
            pipe = coord_get(coord, data)
            dist += 1
            
            if pipe == -1:
                print(f"  Hit wall at {coord}. Returning to start")
                break

        if pipe == 'S':
            print(f"Start found at distance {dist}")
            break

    print(f"\nFarthest loop distance is {dist//2}")


def coord_get(coord, data):

    if coord[0] < 0 or coord[0] >= len(data) or coord[1] < 0 or coord[1] >= len(data[0]):
        return -1

    return data[coord[0]][coord[1]]    


def add_coords(a, b):
    return (a[0] + b[0], a[1] + b[1])

    
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

