#!/usr/bin/python3
"""Defines a fuNction that determines if a box containing a list
   of lists can be opened using keys stored in the lists
"""
def canUnlockAll(boxes):
    """Determines if boxes can be unlocked"""
    n = len(boxes)
    unlocked = set([0])  # Start with box 0 unlocked.
    keys = [0]  # Start with the key to box 0.

    while keys:
        current_key = keys.pop()
        
        # Iterate over the keys in the current box.
        for key in boxes[current_key]:
            # If the key corresponds to a box that hasn't been unlocked yet:
            if key not in unlocked and key < n:
                unlocked.add(key)  # Unlock the box.
                keys.append(key)  # Add its keys to the list to explore.
    
    # If the number of unlocked boxes equals the total number of boxes, return True.
    return len(unlocked) == n
