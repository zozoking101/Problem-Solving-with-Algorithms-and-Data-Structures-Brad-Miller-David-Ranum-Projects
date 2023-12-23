from random import choice

def linear_select(arr, k):
    """
    Find the kth smallest element in the list using linear-time algorithm.

    Parameters:
    - arr: The list of numbers.
    - k: The position of the desired smallest element (1-based index).

    Returns:
    - The kth smallest element.
    """
    if not (1 <= k <= len(arr)):
        raise ValueError("Invalid value of k")

    pivot = choice(arr)

    # Partition the list into three parts: elements smaller, equal, and greater than the pivot
    smaller = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    larger = [x for x in arr if x > pivot]

    if k <= len(smaller):
        return linear_select(smaller, k)
    elif k <= len(smaller) + len(equal):
        return pivot
    else:
        return linear_select(larger, k - len(smaller) - len(equal))

# Example usage
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
k = 3
result = linear_select(my_list, k)
print(f"The {k}th smallest number is: {result}")
