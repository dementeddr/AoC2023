#!/usr/bin/python3

import sys
import re

_day = 2 #Advent of Code day

def main(input_file):
    
    data = []

    with open(input_file, "r") as fp:
        data = fp.readlines()

    power_total = 0
    game_pat = re.compile(r"^Game (\d+):")
    cube_pat = re.compile(r" (\d+) (\w+)")


    for line in data:

        mins = {
            "red":0,
            "green":0,
            "blue":0,
        }

        game = int(game_pat.match(line).group(1))
        cubes = cube_pat.findall(line)

        for pull in cubes:
            num = int(pull[0])
            if num > mins[pull[1]]:
                mins[pull[1]] = num

        power = 1

        for color in mins:
            power = power * mins[color]

        power_total += power

    print(f"Power Total = {power_total}")
                


if __name__ == "__main__":
    input_file = f"input-d{_day}.txt"

    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    main(input_file)
