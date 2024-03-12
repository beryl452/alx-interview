#!/usr/bin/python3
"""
0-lockboxes.py
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    Return True if all boxes can be opened, else return False
    """
    for i in range(0, len(boxes)):
        if ((i != len(boxes) - 1) and not boxes[i]):
            return False
    return True
