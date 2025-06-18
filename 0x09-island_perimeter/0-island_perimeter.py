#!/usr/bin/python3
"""
Module 0-island_perimeter
Provides a function to calculate the perimeter of an island in a grid.
"""

def island_perimeter(grid):
    """
    Calculates the perimeter of an island.
    Grid is a list of lists of integers (0 = water, 1 = land).
    Returns the perimeter as an integer.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4

                # Check up
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 1
                # Check down
                if row < rows - 1 and grid[row + 1][col] == 1:
                    perimeter -= 1
                # Check left
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 1
                # Check right
                if col < cols - 1 and grid[row][col + 1] == 1:
                    perimeter -= 1

    return perimeter
