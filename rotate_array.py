# rotate_array.py

def  rotate_array(nums, k):
    k = k % len(nums)
    return nums[-k:] + nums[:-k]

print(rotate_array([1, 2, 3, 4, 5], 2))
