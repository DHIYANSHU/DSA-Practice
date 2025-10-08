# linear_search.py

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# test     
nums = [5, 3, 8, 6, 7]
print(linear_search(nums, 6))
print(linear_search(nums, 10))
