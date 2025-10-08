#max_in_list.py
def find_max(nums):
    if not nums:
        return None
    maximum = nums[0]
    for n in nums:
        if n > maximum:
            maximum = n
    return maximum

if __name__ == "__main__":
    arr = [3, 7, 2, 9, 5]
    print("array:", arr)
    print("max:", find_max(arr))
