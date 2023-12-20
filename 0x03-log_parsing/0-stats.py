#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics organized as follows:
    file size
    http status code, total number
Possible status codes: 200, 301, 400, 401, 403, 404, 405 and 500
"""
import sys


counter = 0
file_size = 0
status_map = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}


def print_stats():
    """Print the currents statistics"""
    print(f"File size: {file_size}")
    for status, count in status_map.items():
        if count > 0:
            print(f"{status}: {count}")


try:
    for line in sys.stdin:
        if counter == 10:
            print_stats()
            counter = 0
        line = line.rstrip()
        line_details = line.split()

        # update status code and line counter if line is in correct format
        if len(line_details) > 4:
            file_size += int(line_details[-1])
            code = line_details[-2]
            if status_map.get(code, None) is not None:
                status_map[code] += 1
            counter += 1
except Exception:
    pass
finally:
    print_stats()
