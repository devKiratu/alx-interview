#!/usr/bin/python3
"""
Defines a method for validating if data is of valid utf8 encoding
"""


def validUTF8(data):
    """
    determines if a given data set represents a valid UTF-8 encoding
    """
    bin_data = []
    for item in data:
        bin_item = bin(item)[2:]
        bin_data.append(bin_item[-8:])
    result = []
    i = 0
    try:
        while i < len(bin_data):
            # check for 1-byte character
            if len(bin_data[i]) <= 7:
                i += 1
                continue
            # check for 2-byte character
            if bin_data[i][0:3] == '110':
                if bin_data[i + 1][0:2] == '10':
                    i += 2
            else:
                return False
            # check for 3-byte character
            if bin_data[i][0:4] == '1110':
                if bin_data[i + 1][0:2] == '10' and\
                 bin_data[i + 2][0:2] == '10':
                    i += 3
                else:
                    return False
            # check for 4-byte character
            if bin_data[i][0:5] == '11110':
                if bin_data[i + 1][0:2] == '10' and\
                  bin_data[i + 2][0:2] == '10' and\
                  bin_data[i + 3][0:2] == '10':
                    i += 4
                else:
                    return False
        return True
    except Exception:
        return False
