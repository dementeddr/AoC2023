#!/usr/bin/python3

import sys
import re
from time import perf_counter_ns
from functools import cmp_to_key

_day = 7 #Advent of Code day

## BEGIN SOLUTION

card_values = {
    "A":14,
    "K":13,
    "Q":12,
    "J":11,
    "T":10,
}


def main(data):

    hands = []

    for line in data:
        tokens = line.split()
        hand = (tokens[0], int(tokens[1]))
        hands.append(hand)

    hands.sort(key=cmp_to_key(compare_hands))

    total_bids = 0

    for i in range(len(hands)):
        total_bids += hands[i][1] * (i+1)
        print(f"{hands[i][0]}  ->  {hands[i][1]} * {i+1} = {total_bids}")

    print(f"Bid Total: {total_bids}")


def compare_hands(x, y):
    handx = hand_type(x[0])
    handy = hand_type(y[0]) #lol
    print(f"{x} -> {handx}")
    print(f"{y} -> {handy}")
    print()
    
    for i in range(5,0,-1):
        diff = len(handx[i]) - len(handy[i])
        #print(f" {i} {diff}")
        if diff != 0:
            return diff
       
        # if len(hand[i]) == 0

    for j in range(5):
        diff = value_card(x[0][j]) - value_card(y[0][j])
        if diff != 0:
            return diff

    return 0
    

def hand_type(hand):
    print(hand)
    adhn = sorted(hand)
    streak = adhn[0]
    count = 0
    breakdown = {
        5:[],
        4:[],
        3:[],
        2:[],
        1:[]
    }
    
    for card in adhn:
        if streak == card:
            count += 1
        else:
            breakdown[count].append(value_card(streak))
            #print(f"{streak} {count}")
            count = 1
            streak = card

    print(f"{streak} {count}")
    breakdown[count].append(value_card(streak))

    #for thing in breakdown:
    #    breakdown[thing].sort()

    return breakdown


def value_card(x):
    if x in card_values:
        return card_values[x]
    return int(x)


## END SOLUTION

if __name__ == "__main__":
    input_file = f"input-d{_day}.txt"
    data = []

    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    with open(input_file, "r") as fp:
        data = fp.readlines()

    time_start = perf_counter_ns()
    main(data)
    time_stop = perf_counter_ns()

    time = (time_stop - time_start) / 1000000
    print(f"\nExecution took {time:.4f} milliseconds")

