#!/usr/bin/python3

import sys
import re
from time import perf_counter_ns
from collections import deque

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

sides = [(-1,0), (0,1), (1,0), (0,-1)]

def main(data):

    S = (-1, -1)

    data = list(map(str.strip, data))

    print(f"Size: {len(data)} x {len(data[0])}")

    # Find Start
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == 'S':
                S = (y, x)
                print(f"S at {S}")
                break

        if S != (-1,-1):
            break
    
    loop_map = find_true_loop(data, S)
    loop_map = clear_outer_spaces(loop_map, S)
    count = 0

    for y in range(len(loop_map)):
        for x in range(len(loop_map[y])):
            coord = (y, x)
            char = coord_get(coord, loop_map)

            if char == '.':
                if is_inside(coord, loop_map): 
                    count += 1
                else:
                    loop_map[y][x] = ' '
                    

    print_map(loop_map)

    print(f"There are {count} spaces inside the pipe loop")


def is_inside(coord, loop_map):
    
    count = 0

    for y in reversed(range(coord[0])):
        char = loop_map[y][coord[1]]
        if char == ' ':
            break
        if char in '-JL':
            count += 1
    
    return count % 2 != 0



def clear_outer_spaces(loop_map, S):
    
    queue = deque()
    queue.append((0,0))
    i = 0
    while len(queue) > 0:
        coord = queue.popleft()
        cur = coord_get(coord, loop_map)
        if cur != '.':
            continue

        loop_map[coord[0]][coord[1]] = ' '
        
        around = get_surroundings(coord)
        i += 1

        for spot in around:
            adj = coord_get(spot, loop_map)
            if adj == '.':
                queue.append(spot)

    return loop_map



def find_true_loop(data, S):

    starts = get_surroundings(S)
    loop_map = []

    for coord in starts:
        prev_coord = S
        pipe = coord_get(coord, data)
        loop_map = [ ['.']*len(data[0]) for i in range(len(data)) ]
        loop_map[S[0]][S[1]] = 'S'

        print(f"Start at {coord}")
        
        while pipe != 'S':
            
            connectors = list(map(lambda c: add_coords(coord, c), offsets[pipe]))
            if prev_coord not in connectors:
                break

            connectors.remove(prev_coord)
            prev_coord = coord
            loop_map[coord[0]][coord[1]] = pipe
            coord = connectors[0]
            pipe = coord_get(coord, data)
            
            if pipe == -1:
                print(f"  Hit wall at {coord}. Returning to start")
                break

        if pipe == 'S':
            return loop_map
    
    print("Error, no true loop found")
    return None



def get_surroundings(coord):
    
    return list(map(lambda side: add_coords(coord, side), sides))



def coord_get(coord, data):

    if coord[0] < 0 or coord[0] >= len(data) or coord[1] < 0 or coord[1] >= len(data[0]):
        return -1

    return data[coord[0]][coord[1]]    



def add_coords(a, b):
    return (a[0] + b[0], a[1] + b[1])



def print_map(loop_map):
    print()
    for line in loop_map:
        print(''.join(line))


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

