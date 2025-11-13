def binary_search(arr, target):
    """
    Perform binary search on a sorted list to find the index of the target element.

    Parameters:
    arr (list): A sorted list of elements.
    target: The element to search for.

    Returns:
    int: The index of the target if found, else -1.
    """
    # Initialize the search boundaries
    left = 0
    right = len(arr) - 1

    # Continue searching while the search space is valid
    while left <= right:
        # Find the middle index
        mid = (left + right) // 2

        # Check if the middle element is the target
        if arr[mid] == target:
            return mid  # Target found

        # If target is smaller, search the left half
        elif arr[mid] > target:
            right = mid - 1

        # If target is larger, search the right half
        else:
            left = mid + 1

    # Target not found
    return -1


# Example usage:
sorted_list = [1, 3, 5, 7, 9, 11, 13]
target_value = 7
result = binary_search(sorted_list, target_value)

if result != -1:
    print(f"Target {target_value} found at index {result}.")
else:
    print(f"Target {target_value} not found in the list.")