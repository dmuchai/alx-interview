#!/usr/bin/python3
"""Pascal's Triangle generator"""


def pascal_triangle(n):
    """Generates Pascal's triangle up to n rows"""
    if n <= 0:
        return []

    triangle = [[1]]  # First row

    for i in range(1, n):
        row = [1]  # Start each row with 1
        for j in range(1, i):
            # Middle values are sum of two above
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # End each row with 1
        triangle.append(row)

    return triangle
