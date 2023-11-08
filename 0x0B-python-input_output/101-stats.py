#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics.
"""
import sys


def print_metrics(total_size, status_codes):
    """
    Prints the computed metrics.

    Args:
        total_size (int): Total file size.
        status_codes (dict): Dictionary containing the
        count of each status code.
    """
    print(f"File size: {total_size}")
    for code, count in sorted(status_codes.items()):
        print(f"{code}: {count}")


line_count = 0
total_size = 0
status_codes = {}

try:
    for line in sys.stdin:
        line_count += 1
        try:
            parts = line.split()
            size = int(parts[-1])
            status_code = int(parts[-2])
            total_size += size
            if status_code in status_codes:
                status_codes[status_code] += 1
            else:
                status_codes[status_code] = 1

            if line_count % 10 == 0:
                print_metrics(total_size, status_codes)

        except (ValueError, IndexError):
            pass

except KeyboardInterrupt:
    pass

print_metrics(total_size, status_codes)
