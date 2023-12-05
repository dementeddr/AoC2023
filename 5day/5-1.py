#!/usr/bin/python3

import sys
import re
from time import perf_counter_ns

_day = 5 #Advent of Code day

def main(input_file):
    
    data = []

    with open(input_file, "r") as fp:
        data = fp.readlines()

## BEGIN SOLUTION
    # Read input
    seeds = list(map(int, data[0].split(' ')[1:]))

    mapping_list = []
    cur_mapping = []
    data.append("\n")

    for line in data[2:]:
        if len(line) == 1:
            mapping_list.append(sorted(cur_mapping, key=lambda t: t[1]))
            cur_mapping = []
            #print(list(map(lambda t: t[0],mapping_list[-1])))
            #print()
            continue

        tokens = line.split(' ')
        # print(tokens)

        if len(tokens) == 3:
            cur_mapping.append(tuple(map(int, tokens)))
            # print(f"{len(mapping_list)}.{len(cur_mapping)}")

    # Start tracing seeds
    locations = []

    for seed in seeds:
        locations.append(trace_seed(seed, mapping_list))    

    locations.sort()
    print(f"Lowest location = {locations[0]}")

            
def trace_seed(seed, mapping_list):

    print(f"Tracing seed {seed}")
    number = seed
    prev_number = seed

    for mapping in mapping_list:
        # print(f"\tRunning mapping {mapping}")
        for span in mapping:
            # print(f"\t\ttesting span {span}")
            if number < span[1]:
                break
            if number >= span[1] and number <= span[1] + span[2]-1:
                offset = number - span[1]
                # print(f"\t\tOffset = {number} - {span[1]} = {offset}")
                prev_number = number
                number = span[0] + offset
                break

        print(f"\t{prev_number} -> {number}")
        prev_number = number

    print(f"Seed {seed} Location = {number}")
    return number

    
 ## END SOLUTION

if __name__ == "__main__":
    input_file = f"input-d{_day}.txt"

    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    time_start = perf_counter_ns()
    main(input_file)
    time_stop = perf_counter_ns()
    time = (time_stop - time_start) / 1000000
    print(f"Execution took {time:.4f} milliseconds")

