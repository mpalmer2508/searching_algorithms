def sequential_search(values, requested_value):

    for i in range(len(values)):
        if values[i] == requested_value:
            return i
    return -1
