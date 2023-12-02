#!/usr/bin/python3

import sys
import re

_day = 2 #Advent of Code day

def main(input_file):
    
    data = []

    with open(input_file, "r") as fp:
        data = fp.readlines()

    id_total = 0
    game_pat = re.compile(r"^Game (\d+):")
    cube_pat = re.compile(r" (\d+) (\w+)")

    maxes = {
        "red":12,
        "green":13,
        "blue":14,
        }

    for line in data:
        game = int(game_pat.match(line).group(1))
        cubes = cube_pat.findall(line)
        isValid = True


        for pull in cubes:
            if int(pull[0]) > maxes[pull[1]]:
                isValid = False
                break

        if isValid:
            print(f"Game {game}: possible {cubes}")# The irony here is not lost on me
            id_total += game

    print(f"ID Total = {id_total}")
                


if __name__ == "__main__":
    input_file = f"input-d{_day}.txt"

    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    main(input_file)
