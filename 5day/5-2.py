#!/usr/bin/python3

import sys
import re
from time import perf_counter_ns
from functools import reduce

_day = 5 #Advent of Code day

def main(input_file):
    
    data = []

    with open(input_file, "r") as fp:
        data = fp.readlines()

## BEGIN SOLUTION

    # Read input
    seed_pat = re.compile(r"(\d+) (\d+)")
    seed_spans = list(map(lambda m: (int(m[0]), int(m[0]) + int(m[1]) - 1), seed_pat.findall(data[0])))
    print(f"Seeds {seed_spans}\n")

    mapping_list = []
    cur_mapping = {}
    data.append("\n")

    # Create mapping ranges
    for line in data[2:]:
        if len(line) == 1:
            mapping_list.append(cur_mapping)
            
            k = sorted(cur_mapping.keys())[-1]
            print(f"  COMPLETE MAPPING. Last mapping[{k}] = {cur_mapping[k]}")

            cur_mapping = {}
            cur_mapping[0] = 0
            continue

        tokens = line.strip().split(' ')
        # print(tokens)

        if len(tokens) == 3:
            map_src = int(tokens[1])
            map_dst = int(tokens[0])
            map_rng = int(tokens[2])
            
            map_end = map_src + map_rng
            offset = map_dst - map_src

            cur_mapping[map_src] = offset
            if map_end not in cur_mapping:
                cur_mapping[map_end] = 0

            print(f"Converted {tokens} -> (mapping[{map_src}] = {offset:+d}, mapping[{map_end}] = {cur_mapping[map_end]})")

    print_seed_total(seed_spans)

    # Start tracing seed spans
    for mapping in mapping_list:
        new_spans = []
        print("\n\nNEXT MAPPING")

        for span in seed_spans:
            print(f"Mapping span {span}")
            returned = map_seed_span(span, mapping)
            print(f"Returned {returned}")
            new_spans += returned
            

        seed_spans = new_spans
        seed_spans.sort()
        seed_spans = print_seed_total(seed_spans)

    # Find lowest and print
    print()
    print()
    print_seed_total(seed_spans)
    print(f"Lowest location = {seed_spans[0][0]}")
            

def map_seed_span(span, mapping):

    # keys is a sorted list of all numbers where the offset changes, which are stored in the mapping dict
    keys = sorted(mapping.keys())
    print(keys)
    start_found = False
    new_spans = []

    for i in range(1, len(keys)):
        rng_start = keys[i-1]
        rng_end = keys[i] - 1
        offset = mapping[rng_start]
        print(f"  ({rng_start}, {rng_end}) = {offset:+d}")

        if span[0] > rng_end:
            continue

        if span[0] <= rng_end and not start_found:
            if span[1] <= rng_end:
                start = span[0] + offset
                end = span[1] + offset
                print(f"    Add single span {(start, end)} and return")
                return [(start, end)]
            else:
                start = span[0] + offset
                end = rng_end + offset
                new_spans.append( (start, end) )
                print(f"    Add first span {new_spans[-1]}")
                start_found = True
                continue
        
        if span[1] <= rng_end:
            start = rng_start + offset
            end = span[1] + offset
            new_spans.append( (start, end) )
            print(f"    Add end span {new_spans[-1]} and return")
            return new_spans

        else:
            start = rng_start + offset
            end = rng_end + offset
            new_spans.append( (start, end) )
            print(f"    Add mid span {new_spans[-1]}")

    if span[0] < keys[-1]:
        new_spans.append( (keys[-1], span[1]) )
        print(f"    Add last span {new_spans[-1]} and return")
    else:
        new_spans.append( (span[0], span[1]) )
        print(f"    Add last span {new_spans[-1]} and return")
    
    return new_spans


def print_seed_total(seed_spans):
    
    seed_spans.sort()
    seed_total = 0 
    reduced = [(0,0)]
   
    for seed in seed_spans:
        seed_total += seed[1] - seed[0] + 1

        if seed[0] == reduced[-1][1]+1:
            old = reduced[-1]
            reduced = reduced[:-1]
            reduced.append((old[0], seed[1]))
        else:
            reduced.append(seed)
    
    seed_spans = sorted(seed_spans, key=lambda ss: ss[0])
    print(f"seed spans {seed_spans}")
    print(f"reduced spans {reduced[1:]}")
    print(f"seed total {seed_total}")

    return reduced


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

