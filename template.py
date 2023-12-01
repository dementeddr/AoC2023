#!/usr/bin/python3

import sys

_day = $$ #Advent of Code day

def main(input_file):
    
    data = []

	with open(input_file, "r") as fp:
        data = fp.readlines()



if __name__ == "__main__":
	input_file = f"input-d{_day}.txt"

	if len(sys.argv) > 1:
		input_file = sys.argv[1]

	main(input_file)
