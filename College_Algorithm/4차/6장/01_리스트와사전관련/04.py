def heapify(arr, idx, size):
    largest = idx
    left_idx = 2 * idx + 1
    right_idx = 2 * idx + 2
    if left_idx < size and arr[left_idx] > arr[largest]:
        largest = left_idx
    if right_idx < size and arr[right_idx] > arr[largest]:
        largest = right_idx
    if largest != idx:
        arr[largest], arr[idx] = arr[idx], arr[largest]
        heapify(arr, largest, size)
def heap_sort(arr, k):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, i, n)
    for i in range(n - 1, 0 , -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)
    return arr[k - 1]