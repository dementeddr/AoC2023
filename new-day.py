#!/usr/bin/python3

import requests
import os
import sys
from dotenv import load_dotenv
import json

day = 0

if len(sys.argv) == 2:
    day = sys.argv[1]
else:
    print("Please enter a day number")
    exit()

print("Reading env variables")
load_dotenv()
year = os.getenv("YEAR")
monster = {"session" : os.getenv("COOKIE")}

dir_name = f"{day}day"

print(f"Making directory: \"{dir_name}\"")
os.mkdir(dir_name)

print("Copying template file")
template = ''

with open(f"template.py") as t_fp:
    template = t_fp.read()

template = template.replace('$$', day)

with open(f"{dir_name}/{day}-1.py", "w") as p_fp:
    p_fp.write(template)

os.chmod(f"{dir_name}/{day}-1.py", 0o777)

print(f"Requesting input file for {year}, day {day}")
input_file = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies=monster)
print(f"Response code: {input_file.status_code}")

if input_file.status_code != 200:
    con = input("Cannot access input file. Continue? [y/N]: ")
    if con not in ('Y', 'y'):
        exit()
    
else:
    print("Writing input file")
    with open(f"{dir_name}/input-d{day}.txt", "w") as in_fp:
        in_fp.write(input_file.text)

print("Done")
