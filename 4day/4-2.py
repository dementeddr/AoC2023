#!/usr/bin/python3

import sys
import re

_day = 4 #Advent of Code day

def main(input_file):
    
    data = []

    with open(input_file, "r") as fp:
        data = fp.readlines()

    card_pat = re.compile(r"^Card\s*(\d+): ([0-9 ]*) \| ([0-9 ]*)$")
    num_pat = re.compile(r"\d+")

    cards = {}
    card_counts = {}
    
    # Intake cards
    for line in data:
        matches = card_pat.match(line)
        card_num = int(matches.group(1))
        winnums = list(map(int, num_pat.findall(matches.group(2))))
        my_nums = list(map(int, num_pat.findall(matches.group(3))))

        cards[card_num] = (winnums, my_nums)
        card_counts[card_num] = 1

    # process cards and count
    total = 0

    for card_num in cards:
        wins = find_wins(cards[card_num][0], cards[card_num][1]) 
        print(f"Card {card_num} has {wins} wins and {card_counts[card_num]} copies. Cur total = {total}")

        for num in range(card_num + 1, card_num + wins + 1):
            card_counts[num] += card_counts[card_num]
            print(f"\tCard {num} now has {card_counts[num]} copies")

        total += card_counts[card_num]

    # output
    print(f"Total number of cards = {total}")


def find_wins(winnums, my_nums):
    
    wins = 0

    for num in my_nums:
        if num in winnums:
            wins += 1

    return wins

    

if __name__ == "__main__":
    input_file = f"input-d{_day}.txt"

    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    main(input_file)
