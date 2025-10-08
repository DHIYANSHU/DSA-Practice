# binary_search_recursive.py

def binary_search_recursive(arr, low, high, target):
    if low > high:
        return-1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, mid + 1, high, target)
    else:
        return binary_search_recursive(arr, low, mid - 1, target)
    

#test
nums = [1, 3, 5, 7, 9]
print(binary_search_recursive(nums, 0, len(nums)-1, 7))
print(binary_search_recursive(nums, 0, len(nums)-1, 2))
