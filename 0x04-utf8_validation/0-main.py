#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))

# more test data
# Incomplete multi-byte character at the end:
data = [195, 66, 67, 68, 69]
print(validUTF8(data))  # Expected output: False

# Invalid multi-byte character: An invalid multi-byte character with the first byte missing.
data = [206, 145]
print(validUTF8(data))  # Expected output: True

# Overlong encoding: Using an overlong encoding for the character 'A'.
data = [192, 128, 65]
print(validUTF8(data))  # Expected output: True

# Mixed valid and invalid characters: A mix of valid and invalid characters.
data = [72, 101, 108, 108, 195, 66, 67, 68, 69]
print(validUTF8(data))  # Expected output: False

# Invalid multi-byte character at the beginning:
data = [206, 66, 67, 68, 69]
print(validUTF8(data))  # Expected output: False

# from leetcode
data = [197,130,1]
print(validUTF8(data), True)

data = [235,140,4]
print(validUTF8(data), False)

# my test cases
data = [130]
print(validUTF8(data), False)

data = [256]
print(validUTF8(data), True)
