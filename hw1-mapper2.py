#!/usr/bin/env python3
from csv import reader
import sys

for line in reader(sys.stdin):
    try:
        date = line[1].strip()
        crime = line[7].strip()
        if not date or not crime or crime != "DANGEROUS WEAPONS":
            continue
        month = date.split('/')[0]
        print(f"{month}\t1")
    except IndexError:
        continue
