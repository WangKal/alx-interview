#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """
    a function that returns a list pascal triangle intergers of n:
       . Returns an empty list if n <= 0
       . assume n will be always an integer
    """
    pascal_tri = []

    if n <= 0:
        return []

    for i in range(n):
        if (i == 0):
            pascal_tri.append([1])
        else:
            _row = []
            for j in range(i + 1):
                if (j == 0 or j == i):
                    _row.append(1)
                else:
                    _row.append(pascal_tri[i - 1][j - 1] +
                                   pascal_tri[i - 1][j])

            pascal_tri.append(_row)

    return (pascal_tri)
