#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
  """
  Returns a list of integers
  representing the Pascal Triangle of n
  returns empty list if n <= 0
  """
  if n <= 0:
    return []
  elif n == 1:
    return [[1]]
  else:
    triangle = [[1]]
    for i in range(1, n):
      prev_row = triangle[-1]
      new_row = [1]
      for j in range(1, i):
        new_row.append(prev_row[j-1] + prev_row[j])


      new_row.append(1)
      triangle.append(new_row)
    return triangle
