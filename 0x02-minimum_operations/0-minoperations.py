#!/usr/bin/python3
"""
This module contains a function that determines the minimum number of
operations required to perform a task
"""


def minOperations(n):
    """
    Returns the fewest steps required to print H exactly n times or 0
    """
    total_printed = 1
    clipboard = 0
    steps = 0

    while total_printed < n:
        if n % total_printed == 0:
            # copy_all
            clipboard = total_printed
            steps += 1
        # paste
        total_printed += clipboard
        steps += 1

    return steps if total_printed == n else 0
