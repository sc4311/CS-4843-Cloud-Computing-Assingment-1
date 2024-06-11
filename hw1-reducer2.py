#!/usr/bin/env python3
import sys

# Mapping month numbers to month names
month_map = {
    '01': 'January', '02': 'February', '03': 'March', '04': 'April',
    '05': 'May', '06': 'June', '07': 'July', '08': 'August',
    '09': 'September', '10': 'October', '11': 'November', '12': 'December'
}

current_month = None
current_count = 0
month = None

for line in sys.stdin:
    line = line.strip()
    month, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue

    if current_month == month:
        current_count += count
    else:
        if current_month:
            print(f"{month_map.get(current_month, 'Unknown')}  {current_count}")
        current_count = count
        current_month = month

if current_month == month:
    print(f"{month_map.get(current_month, 'Unknown')}  {current_count}")
