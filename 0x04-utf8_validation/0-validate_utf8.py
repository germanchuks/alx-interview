#!/usr/bin/python3
"""
Module to determine if a given data set represents a valid UTF-8 encoding.
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """Returns True if a data is a valid UTF-8 encoding."""
    num_bytes = 0

    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for byte in data:
        mask_byte = 1 << 7

        if num_bytes == 0:
            while mask_byte & byte:
                num_bytes += 1
                mask_byte >>= 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            if not (byte & mask_1 and not (byte & mask_2)):
                return False

        num_bytes -= 1

    return num_bytes == 0
