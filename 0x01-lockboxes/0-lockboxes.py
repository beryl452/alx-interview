#!/usr/bin/python3
"""
0-lockboxes.py
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    Return True if all boxes can be opened, else return False
    """
    boxeLength = len(boxes)
    if boxeLength == 0:
        return True
    unlocked = [False] * boxeLength
    unlocked[0] = True
    keys = boxes[0]

    while keys:
        key = keys.pop()
        if key < boxeLength and not unlocked[key]:
            unlocked[key] = True
            keys += boxes[key]

    return all(unlocked)
