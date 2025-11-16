def heapify(arr, n, i):
    largest = i       # Initialize largest as root
    left = 2 * i + 1   # Left child
    right = 2 * i + 2  # Right child

    # Check if left child is larger
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child is larger
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If root is not largest, swap and heapify
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap root with end
        heapify(arr, i, 0)


data = [12, 11, 13, 5, 6, 7]
heap_sort(data)
print("Heap Sorted:", data)