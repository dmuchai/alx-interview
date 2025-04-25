#!/usr/bin/python3
"""Determines if all boxes can be opened"""

def canUnlockAll(boxes):
        """
    Determines if all locked boxes can be opened
    based on keys that can be attained.
    Solution to the lockboxes problem
    """
    if not boxes or not isinstance(boxes, list):
        return False

    n = len(boxes)
    visited = set([0])  # Start with box 0

    stack = [0]  # DFS approach

    while stack:
        current = stack.pop()
        for key in boxes[current]:
            if key not in visited and 0 <= key < n:
                visited.add(key)
                stack.append(key)

    return len(visited) == n
