#!/usr/bin/env python3
import sys
from collections import defaultdict

bur_crime_count = defaultdict(int)
bur_crime_types = defaultdict(set)

for line in sys.stdin:
    line = line.strip()
    bro, crime_type = line.split('\t', 1)
    bur_crime_count[bro] += 1
    bur_crime_types[bro].add(crime_type)

# Determine the borough with the highest number of crimes
most_crime_bro = None
most_crime_count = 0
for boro, count in bur_crime_count.items():
    if count > most_crime_count:
        most_crime_bro = boro
        most_crime_count = count

# Print the results
if most_crime_bro:
    print(f"Most of the crimes were reported in {most_crime_bro}.")
    print()
    print(f"Total number of crimes reported in {most_crime_bro} is {most_crime_count}.")
    print()
    print(f"Crime types reported in {most_crime_bro} are: {', '.join(bur_crime_types[most_crime_bro])}.")






