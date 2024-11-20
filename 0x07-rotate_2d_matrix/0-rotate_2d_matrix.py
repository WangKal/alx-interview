#!/usr/bin/python3
"""
This module provides an algorithm to rotate a 2D array 90° clockwise.

APPROACH:
    - Normalize the 2D array to a 1D representation by mapping each (row, col) 
      pair to a single index:
        - row_index = index // width
        - col_index = index % width
    - Compute all indices (total: width * height) and map each to:
        - Its new position after rotation.
        - Its value in the original array.
    - Use the map to place values in their new positions.

FUNCTIONS:
    rotate_2d_matrix:
        - Main function that executes the rotation.

    build_map:
        - Maps each index to its new position and value.
        Structure:
        {
            index: {
                'new_index': new normalized position,
                'value': value at the index
            }
        }

    get_new_index:
        - Computes the new index for a given normalized index:
            - new_col_index = width - 1 - row_index
            - new_row_index = col_index
        - Combines them to calculate the new normalized index.

    get_value:
        - Converts a normalized index to (row, col) to retrieve its value.

    compute_row_and_col:
        - Converts a normalized index to its (row, col) pair.
"""



def rotate_2d_matrix(m):
    """main function: rotates a 2d array 90 deg"""
    width = len(m[0])
    height = len(m)
    total_items = width * height
    map_ = build_map(m, total_items, width)
    # print(map_)
    for index in map_:
        prev_index = index
        value = map_[prev_index]["value"]
        new_index = map_[prev_index]["new_index"]
        row, index = compute_row_and_index(new_index, width)
        m[row][index] = value


def build_map(m, length, width):
    """returns a map of prev_index and their
    next positions"""
    dct = {
        i: {
            "new_index": get_new_index(i, width),
            "value": get_value(m, i, width)
        }
        for i in range(length)
    }
    return dct


def get_new_index(i, width):
    """computes new position"""
    current_index = i % width
    current_row = int(i / width)
    next_index = width - 1 - current_row
    next_row = current_index
    next_position = next_row * width + next_index
    return next_position


def get_value(m, i, width):
    """gets the value of a 2d array by denormalizing
    its flattened index"""
    current_index = i % width
    current_row = int(i / width)
    return m[current_row][current_index]


def compute_row_and_index(flat_index, width):
    """returns denormalized row and index from a
    flattened 2d array index"""
    row = int(flat_index / width)
    index = flat_index % width
    return row, index


def printx(lst):
    """custom print function to print 2d array"""
    print("[")
    for itm in lst:
        print("  ", str(itm) + ",")
    print("]")


def build_matrix(n):
    """ builds n * n 2d matrix """
    parent = []
    y = 1
    for i in range(n):
        child = []
        for x in range(y, n * n + 1):
            child.append(x)
            if x % n == 0 and x != 1:
                y = x + 1
                break
        parent.append(child)
    return parent


if __name__ == "__main__":
    matrix = build_matrix(3)

    rotate_2d_matrix(matrix)
    printx(matrix)
    print()
    matrix = build_matrix(5)

    rotate_2d_matrix(matrix)
    printx(matrix)
