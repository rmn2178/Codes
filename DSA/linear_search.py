def linear_search(arr, target):
    """
    Performs a linear search on the given list to find the target value.

    Parameters:
    arr (list): The list of elements to search through.
    target (any): The value to search for in the list.

    Returns:
    int: The index of the target if found, otherwise -1.
    """

    # Loop through each element in the list using its index
    for index in range(len(arr)):
        # Debug print (optional): show current element being compared
        # print(f"Checking index {index}: value = {arr[index]}")

        # Check if the current element matches the target
        if arr[index] == target:
            # If found, return the index immediately
            return index

    # If the loop completes without finding the target, return -1
    return -1



# Sample list to search
numbers = [10, 25, 30, 45, 50, 65]

# Target value to find
search_value = 45

# Call the linear_search function
result = linear_search(numbers, search_value)

# Output the result
if result != -1:
    print(f"Target {search_value} found at index {result}.")
else:
    print(f"Target {search_value} not found in the list.")