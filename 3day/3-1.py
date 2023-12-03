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

    for y in range(len(data)):

        prev_char = '.'
        symbol_found = False
        number = ""

        for x in range(len(data[y])):

            if data[y][x] in string.digits: 
                
                if prev_char not in string.digits and check_around(x-1, y, data, True):
                    symbol_found = True

                if check_around(x, y, data, False):
                    symbol_found = True

                number += data[y][x]

            elif prev_char in string.digits:
                
                if check_around(x, y, data, True):
                    symbol_found = True

                if symbol_found == True:
                    part_total += int(number)
                
                number = ""
                symbol_found = False

            prev_char = data[y][x]


    print(f"Part Number Total = {part_total}")


def check_around(x, y, data, and_center):

    if x < 0 or x >= len(data):
        return False 

    if y > 0 and is_symbol(data[y-1][x]):
        return True
        
    if y < len(data) - 1 and is_symbol(data[y+1][x]):
        return True

    if and_center and is_symbol(data[y][x]):
        return True

    return False
        
            

def is_symbol(char):
    
    if char == '.' or char in string.digits:
        return False

    return True



if __name__ == "__main__":
    input_file = f"input-d{_day}.txt"

    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    main(input_file)
