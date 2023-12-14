#!/usr/bin/python3
"""
This module contains a function that determines the minimum number of
operations required to perform a task
"""


def minOperations(n: int) -> int:
    """
    Returns the fewest steps required to print H exactly n times
    or 0 if impossible
    """
    total_printed: int = 1
    clipboard: int = 0
    steps = 0

    def copy_all():
        """helper function to simulate copy operations"""
        nonlocal clipboard, steps
        if clipboard == 0:
            clipboard += 1
        else:
            clipboard += clipboard
        steps += 1

    def paste():
        """helper function to simulate paste operation"""
        nonlocal total_printed, steps
        total_printed += clipboard
        steps += 1

    if n <= 1:
        return 0

    while total_printed < n:
        if clipboard == 0:
            copy_all()
            paste()
        if (n - total_printed) % total_printed == 0:
            copy_all()
        paste()

    return steps
