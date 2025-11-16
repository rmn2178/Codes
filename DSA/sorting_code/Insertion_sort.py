def insertion_sort(arr):
    # Traverse from the second element to the end
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be inserted
        j = i - 1

        # Move elements of arr[0..i-1] that are greater than key
        # one position ahead to make space for the key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Place the key at its correct position
        arr[j + 1] = key

# Data
data = [12, 11, 13, 5, 6]

# Passing the data through the function
insertion_sort(data)

# Printing the sorted array
print("Sorted array:", data)