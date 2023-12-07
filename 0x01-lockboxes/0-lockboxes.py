#!/usr/bin/python3
"""
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes
This module contains the solution to the above puzzle
"""


def canUnlockAll(boxes):
    """determines if all the boxes can be opened"""
    num_boxes = len(boxes)
    if num_boxes == 1:
        return True

    keys = set(boxes[0])
    open_boxes = [False for i in range(num_boxes)]

    # the first box is open
    open_boxes[0] = True

    while True:
        # update this with keys found in newly opened boxes
        new_keys = set()

        # open the first set of boxes
        for key in keys:
            if key < num_boxes and not open_boxes[key]:
                open_boxes[key] = True
                new_keys.update(boxes[key])

        # no more keys found
        if not new_keys:
            break
        # add new keys to the iteration set
        keys.update(new_keys)

    return all(open_boxes)
