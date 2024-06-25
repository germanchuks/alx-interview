#!/usr/bin/python3
""" Module to determine the perimeter of an island described using a grid.
"""


def island_perimeter(grid):
    """ Returns the perimeter of the island described in `grid`.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4

                # Check the cell above
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 1
                # Check the cell below
                if r < rows - 1 and grid[r + 1][c] == 1:
                    perimeter -= 1
                # Check the left cell
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 1
                # Check the right cell
                if c < cols - 1 and grid[r][c + 1] == 1:
                    perimeter -= 1

    return perimeter
