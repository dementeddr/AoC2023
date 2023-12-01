#!/usr/bin/python3

import sys
import re

day = 1 #Advent of Code day

def main(input_file):

    total = 0
    pattern = re.compile(r"\d")

    with open(input_file, "r") as fp:
        
        for line in fp:
            digits = pattern.findall(line)
            total += int(digits[0] + digits[-1])

    print(f"Total = {total}")


if __name__ == "__main__":
    input_file = f"input-d{day}.txt"

    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    main(input_file)
