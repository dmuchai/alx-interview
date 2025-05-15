#!/usr/bin/python3
"""
UTF-8 Validation
"""

def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding."""
    num_bytes = 0

    for byte in data:
        # Only consider the 8 least significant bits
        byte = byte & 0xFF

        if num_bytes == 0:
            # Count the number of leading 1's
            if (byte >> 7) == 0:
                continue
            elif (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            else:
                return False
        else:
            # Check that the byte starts with 10xxxxxx
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
