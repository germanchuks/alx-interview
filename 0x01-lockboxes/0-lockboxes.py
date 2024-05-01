#!/usr/bin/python3
"""
Determines if all boxes numbered sequentially from 0 to n-1 can be
opened. Each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """Method to determine if all boxes can be opened"""

    # Check is boxes is a list of lists
    if not (isinstance(boxes, list) and
            all(isinstance(box, list) for box in boxes)):
        return False

    opened_boxes = {0}

    keys = set(boxes[0])

    while keys:
        key = keys.pop()
        if key < len(boxes):
            opened_boxes.add(key)
            keys.update(boxes[key])

    # Check if all boxes have been opened
    return len(opened_boxes) == len(boxes)
