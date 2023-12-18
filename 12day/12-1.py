#!/usr/bin/python3

import sys
import re
from time import perf_counter_ns

_day = 12 #Advent of Code day
log_level = 4

## BEGIN SOLUTION


num_pat = re.compile(r"\d+")
spring_pat = re.compile(r"([#?]+)")

def main(data):

    combos = 0

    for line in data:
         
        halves = line.split()
        nums = list(map(int,num_pat.findall(halves[1])))
        springs = halves[0]
 
        log(1, f"\nNEXT LINE: {springs}  {nums}")
        fits = does_fit(springs, nums, '  ')
        combos += fits
        log(1, f"{fits} <- fits. Total = {combos}")

    print(f"\nTotal possible combinations = {combos}")



def does_fit(section, nums, indent):
    if len(nums) == 0:
        log(4, f"{indent}No nums. Returning 0")
        return 0

    total_len = sum(nums) + len(nums) -1
    total_fits = 0

    log(2, f"{indent}{section} - {len(section)},  {nums} - {total_len}")
    
    if total_len > len(section):
        log(4, f"{indent}Too long. Returning 0")
        return 0

    for i in range(len(section) - total_len + 1):
        space = i+nums[0]
        span = section[i:space]
        log(3, f"{indent}{section} {nums}")
        log(3, f"{indent}i={i} {span} + {section[space] if space < len(section) else ' '}")

        if i > 0 and section[i-1] == '#':
            log(4, f"{indent}Leaving bare spring")
            break

        if '.' in span:
            log(4, f"{indent}Contains '.' Next")
            continue

        if space < len(section) and section[space] == '#':
            log(4, f"{indent}Bare spring. Next")
            continue

        if len(nums) == 1:
            if '#' in section[space:]:
                log(4, f"{indent}Single doesn't cover spring. Next")
            else:
                log(4, f"{indent}Adding 1 fit")
                total_fits += 1
        
        else:
            fit = does_fit(section[space+1:], nums[1:], indent+'  ')
            total_fits += fit
            log(3, f"{indent}fit={fit}, total={total_fits}")

        if section[i] == '#':
            log(4, f"{indent}Leaving bare spring")
            break

    log(2, f"{indent}returning {total_fits}")
    return total_fits


            

    
## END SOLUTION

def log(level, string):

    if level <= log_level:
        print(string)


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

