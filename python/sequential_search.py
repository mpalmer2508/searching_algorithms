def sequential_search(values, requested_value):
    """
    Perform a sequential search to find the index of the requested value in a list.

    Parameters:
    - values (list): The list of values to be searched.
    - requested_value: The target value to be searched for.

    Returns:
    - int: The index of the requested value if found, or -1 if not found.
    """

    for i in range(len(values)):
        if values[i] == requested_value:
            return i
    return -1
