#!/usr/bin/python3
def island_perimeter(grid):
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4

                # Check above
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 1
                # Check below
                if row < rows - 1 and grid[row + 1][col] == 1:
                    perimeter -= 1
                # Check left
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 1
                # Check right
                if col < cols - 1 and grid[row][col + 1] == 1:
                    perimeter -= 1

    return perimeter
