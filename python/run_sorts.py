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
        return_string += f"{duration:0.4f} milliseconds)"
    else:
        return_string += f"{duration:0.4f} seconds)"

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
    start = time.perf_counter()
    found = binary_search(values, x)
    binary_search()
    finish = time.perf_counter()
    run_time = finish - start

    print_string = ""
    if found != -1:
        print_string += f"BST: {x} was found at index {found} ("
    else:
        print_string += f"BST: {x} was not found ("

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
    values = random.sample(range(0, 100), 50)

    x = 37

    # values = ["Ast","ast","brt","ser","Plod"]
    # x = "ast"

    run_bst(sorted(values), x)


if __name__ == "__main__":
    main()
