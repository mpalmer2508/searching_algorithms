import random
import time
from bst import binary_search


def convert_find_time(duration):
    """
    Convert the duration to a human-readable string representation.

    Parameters:
    - duration (float): The duration in seconds.

    Returns:
    - str: A string representation of the duration.
    """
    return_string = ""
    if duration < 0.001:
        duration *= 1000
        return_string += f"{duration:0.4f} milliseconds"
    else:
        return_string += f"{duration:0.4f} seconds"

    return return_string


def run_bst(values, x):
    """
    Run a binary search on a sorted list of values and print the result.

    Parameters:
    - values (list): A list of values to search.
    - x: The value to search for.

    Returns:
    - None
    """
    values = sorted(values) #This consumes a lot of time with large datasets. 
    start = time.perf_counter()
    found = binary_search(values, x)
    finish = time.perf_counter()
    run_time = finish - start

    print_string = ""
    if found:
        print_string += f"BST: {x} was found in "
    else:
        print_string += f"BST: {x} was not found in "

    print_string += convert_find_time(run_time)
    print(print_string)
    


def main():
    """
    Main function to demonstrate binary search on a random list of values.

    Parameters:
    - None

    Returns:
    - None
    """
    values = random.sample(range(1, 1001), 1000)
    values.append(336245)
    x = 336245

    run_bst(values, x)


if __name__ == "__main__":
    main()
