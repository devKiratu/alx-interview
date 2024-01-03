#!/usr/bin/python3
"""
Defines a method for validating if data is of valid utf8 encoding
"""


def validUTF8(data):
    """
    determines if a given data set represents a valid UTF-8 encoding
    """
    return all(i >= 0 and i <= 255 for i in data)
