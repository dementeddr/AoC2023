#!/usr/bin/python3

import sys
import re

_day = $$ #Advent of Code day

def main(input_file):
    
    data = []

    with open(input_file, "r") as fp:
        data = fp.readlines()

    ## BEGIN SOLUTION


    
    ## END SOLUTION

if __name__ == "__main__":
    input_file = f"input-d{_day}.txt"

    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    main(input_file)
