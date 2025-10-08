# binary_search_iterative.py

def binary_search_iterative(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1    
    return -1

#test
nums = [2, 4, 6, 8, 10, 12]
print(binary_search_iterative(nums, 8))
print(binary_search_iterative(nums, 7))
