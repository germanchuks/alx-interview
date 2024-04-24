#!/usr/bin/python3
"""
Function that returns a list of lists of integers representing the Pascal's
triangle of n


STEPS
- Initialize triangle with the first row as base case
- Loop through rows from i = 1 to i = n-1 excluding the first row
- Initialize each row to start with 1
- Loop through elements within the row except the first and last
- Get the previous row for calculation
- Calculate the next element of current row using elements of previous row in
  the current index and previous index
- Add the calculated element to the current row
- Add the final 1 to the end of the row
- Append the completed row to the triangle
- Return the generated triangle
"""

def pascal_triangle(n):
    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            prev_row = triangle[i-1]
            next_item = prev_row[j - 1] + prev_row[j]
            row.append(next_item)
        row.append(1)
        triangle.append(row)
    
    return triangle
