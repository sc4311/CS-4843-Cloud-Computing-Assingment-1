#!/usr/bin/env python3
import sys
from collections import defaultdict

boro_crime_count = defaultdict(int)
boro_crime_types = defaultdict(set)

for line in sys.stdin:
    line = line.strip()
    boro, crime_type = line.split('\t', 1)
    boro_crime_count[boro] += 1
    boro_crime_types[boro].add(crime_type)

# Determine the borough with the highest number of crimes
most_crime_boro = None
most_crime_count = 0
for boro, count in boro_crime_count.items():
    if count > most_crime_count:
        most_crime_boro = boro
        most_crime_count = count

# Print the results
if most_crime_boro:
    print(f"Most of the crimes were reported in {most_crime_boro}.")
    print()
    print(f"Total number of crimes reported in {most_crime_boro} is {most_crime_count}.")
    print()
    print(f"Crime types reported in {most_crime_boro} are: {', '.join(boro_crime_types[most_crime_boro])}.")






