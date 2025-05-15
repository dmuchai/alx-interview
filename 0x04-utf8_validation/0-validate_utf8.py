#!/usr/bin/python3
"""UTF-8 Validation"""


def get_leading_set_bits(num):
    """
    Returns the number of leading set bits (1s) in a byte.
    """
    set_bits = 0
    helper = 1 << 7
    while helper & num:
        set_bits += 1
        helper = helper >> 1
    return set_bits


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    bits_count = 0

    for i in range(len(data)):
        byte = data[i] & 0xFF

        if bits_count == 0:
            bits_count = get_leading_set_bits(byte)

            # 1-byte character (0xxxxxxx)
            if bits_count == 0:
                continue

            # UTF-8 characters must be between 2 and 4 bytes
            if bits_count == 1 or bits_count > 4:
                return False
        else:
            # Check for continuation byte format: 10xxxxxx
            if not (byte & (1 << 7) and not (byte & (1 << 6))):
                return False

        bits_count -= 1

    return bits_count == 0
