def kth_smallest_linearithmic(arr, k):
    """
    Find the kth smallest element in the list using sorting.

    Parameters:
    - arr: The list of numbers.
    - k: The position of the desired smallest element (1-based index).

    Returns:
    - The kth smallest element.
    """
    if not (1 <= k <= len(arr)):
        raise ValueError("Invalid value of k")

    # Sort the list in ascending order
    arr.sort()

    # Return the kth smallest element
    return arr[k - 1]

# Example usage
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
k = 3
result = kth_smallest_linearithmic(my_list, k)
print(f"The {k}th smallest number is: {result}")
