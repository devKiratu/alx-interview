#!/usr/bin/python3
"""
Defines a method for validating if data is of valid utf8 encoding
"""


def validUTF8(data):
    """
    determines if a given data set represents a valid UTF-8 encoding
    """
    last_8 = []
    for item in data:
        bin_item = bin(item)[2:]
        int_item = int(bin_item[-8:], 2)
        last_8.append(int_item)
    return all(i > 0 and i <= 255 for i in last_8)
