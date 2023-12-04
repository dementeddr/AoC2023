#!/usr/bin/python3

import sys
import re

_day = 4 #Advent of Code day

def main(input_file):
    
    data = []

    with open(input_file, "r") as fp:
        data = fp.readlines()

    card_pat = re.compile(r"^.*: ([0-9 ]*) \| ([0-9 ]*)$")
    num_pat = re.compile(r"\d+")

    total_points = 0
    
    for line in data:
        matches = card_pat.match(line)
        #print(f"{matches.group(1)} , {matches.group(2)}")
        winnums = list(map(int, num_pat.findall(matches.group(1))))
        my_nums = list(map(int, num_pat.findall(matches.group(2))))

        card_points = 0

        for num in my_nums:
            if num in winnums:
                card_points = 1 if card_points == 0 else card_points * 2

        total_points += card_points

    print(f"Total Points = {total_points}")

if __name__ == "__main__":
    input_file = f"input-d{_day}.txt"

    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    main(input_file)
