import re
from pprint import pprint

with open('input.txt', 'r') as file:
    for line in file:
        pprint(re.findall("mul\([0-9]*,[0-9]*\)",line))