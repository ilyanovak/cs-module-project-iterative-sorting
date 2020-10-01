def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    start_item = 0
    end_item = len(arr) - 1
    average = end_item // 2
    while start_item < end_item:
        if arr[average] == target: return average
        elif arr[average] > target: end_item = average
        else: start_item = average
        average = average // 2
    return -1  # not found
