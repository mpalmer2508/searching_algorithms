def sentinel_linear_search(values, requested_value):
    """
    Perform a linear search using a sentinel value to find the index of the requested value in a list.

    Parameters:
    - values (list): The list of values to be searched.
    - requested_value: The target value to be searched for.

    Returns:
    - int: The index of the requested value if found, or -1 if not found.
    """
    search_index = 0
    end = values[-1]                
    values[-1] = requested_value    #Sentinel Value
    
    while values[search_index] != requested_value:
        search_index += 1
    
    if search_index < len(values) or values[search_index] == requested_value:
        return search_index
    else:
        return -1

