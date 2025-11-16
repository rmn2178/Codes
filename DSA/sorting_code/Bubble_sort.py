def bubble_sort(arr):
    # Get the length of the array
    n = len(arr)

    # Traverse through all elements in the array
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the current element is greater than the next
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

data = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(data)  # Sort the array in ascending order
print("Sorted array:", data)