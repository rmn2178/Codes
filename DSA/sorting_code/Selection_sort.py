def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Assume the current index is the minimum
        min_idx = i

        # Find the actual minimum element in the remaining unsorted array
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swapping the found minimum element with the first unsorted element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Example usage
data = [64, 25, 12, 22, 11]

# Passing the data to the function
selection_sort(data)

# Printing the sorted array
print("Sorted array:", data)