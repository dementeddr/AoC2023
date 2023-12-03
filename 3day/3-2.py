#!/usr/bin/python3

import sys
import re
import string

_day = 3 #Advent of Code day

def main(input_file):
    
    data = []

    with open(input_file, "r") as fp:
        data = fp.readlines()

    part_total = 0

    parts = {}
    stars = []

    for y in range(len(data)):

        prev_char = '.'
        number = ""
        num_start = 0

        for x in range(len(data[y])):

            if data[y][x] in string.digits: 
                
                if prev_char not in string.digits:
                    num_start = x

                number += data[y][x]

            else:
                
                if data[y][x] == '*':
                    stars.append((x,y))
                    print(f"Star at {stars[-1]}")

                if prev_char in string.digits:
                
                    num_range = (y, num_start, x-1)
                    parts[num_range] = int(number)
                    print(f"{number} is at range {num_range}")
                    number = ""


            prev_char = data[y][x]


    for star in stars:
        
        near_parts = []

        for part in parts:
            
            # print(f"Part {parts[part]} range expansion = ({part[0]-1},{part[1]-1}) - ({part[0]+1},{part[2]+1})")
            if is_near_part(part, star):
                near_parts.append(parts[part])
                # print(f"Star {star} is near {parts[part]} at {part}")

        if len(near_parts) == 2:
            ratio = near_parts[0] * near_parts[1]
            part_total += ratio
            print(f"Star {star} is a gear. Gear ratio: {near_parts[0]} * {near_parts[1]} = {ratio}. Total = {part_total}")

    print(f"Part Number Total = {part_total}")


def is_near_part(part_range, star):

    
    if star[1] < part_range[0] - 1:
        return False

    if star[1] > part_range[0] + 1:
        return False

    if star[0] < part_range[1] - 1:
        return False

    if star[0] > part_range[2] + 1:
        return False

    return True


if __name__ == "__main__":
    input_file = f"input-d{_day}.txt"

    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    main(input_file)
