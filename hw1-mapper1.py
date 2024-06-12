#!/usr/bin/env python3
from csv import reader
import sys

for line in reader(sys.stdin):
    try:
        bur = line[13].strip()
        crime_type = line[7].strip()
        if not bur or bur == "BORO_NM" or not crime_type or crime_type == "OFNS_DESC":
            continue
        print(f"{bur}\t{crime_type}")
    except IndexError:
        continue
