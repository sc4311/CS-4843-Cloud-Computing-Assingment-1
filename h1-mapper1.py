#!/usr/bin/env python3
from csv import reader
import sys

for line in reader(sys.stdin):
    try:
        boro = line[13].strip()
        crime_type = line[7].strip()
        if not boro or boro == "BORO_NM" or not crime_type or crime_type == "OFNS_DESC":
            continue
        print(f"{boro}\t{crime_type}")
    except IndexError:
        continue