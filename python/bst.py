"""Code in python for a Binary Search Tree"""

import time


def binary_search(sorted_array, requested_value, start=0, end=None):
    """
    Perform binary search on a sorted array to find a requested value.

    Arguments:
        sorted_array (list): List of sorted values to search through.
        requested_value: The value to search for.
        start (int, optional): The starting index of the current subarray being considered.
                              Defaults to 0.
        end (int, optional): The ending index of the current subarray being considered.
                            Defaults to the last index of the array.

    Returns:
        int: The index of the requested value if found, or -1 if the value is not in the array.
    """
    if end == None:
        end = len(sorted_array) - 1

    if start > end:
        return -1

    mid = (start + end) // 2
    if sorted_array[mid] == requested_value:
        return mid

    elif sorted_array[mid] < requested_value:
        return binary_search(sorted_array, requested_value, mid + 1, end)
    else:
        return binary_search(sorted_array, requested_value, start, mid - 1)
