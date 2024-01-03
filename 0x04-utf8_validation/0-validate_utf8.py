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
        last_8.append(bin_item[-8:])
    return all(i[0] == '0' or
               i[0:2] == '10' or
               i[0:3] == '110' or
               i[0:4] == '1110' or
               i[0:5] == '11110' for i in last_8)
