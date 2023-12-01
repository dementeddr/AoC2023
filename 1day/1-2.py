#!/usr/bin/python3

import sys
import re

_day = 1 #Advent of Code day
_wordNums = {
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9"
    }

_cruelty = {
    "twone":"twoone",
    "sevenine":"sevennine",
    "oneight":"oneeight",
    "threeight":"threeeight",
    "fiveight":"fiveeight",
    "eightwo":"eighttwo",
    "eighthree":"eightthree"
    }


def main(input_file):

    total = 0
    pattern = re.compile(r"\d|one|two|three|four|five|six|seven|eight|nine")

    with open(input_file, "r") as fp:
        
        for line in fp:
            exp_line = normalize(line[:-1])
            digits = pattern.findall(exp_line + '.')
            pair = getNum(digits[0]) + getNum(digits[-1])
            total += int(pair)
            print(f"{line[:-1]}\t -> {exp_line}\t -> {digits[0]} + {digits[-1]} -> {pair} -> {total}")

    print(f"Total = {total}")


def getNum(word):
    if len(word) == 1:
        return word

    return _wordNums[word]
    

def normalize(word):
    result = word
    for key in _cruelty:
        result = result.replace(key, _cruelty[key])

    return result


if __name__ == "__main__":
    input_file = f"input-d{_day}.txt"

    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    main(input_file)
