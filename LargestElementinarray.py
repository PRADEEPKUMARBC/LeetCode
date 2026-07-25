nums = [74, 85, 12, 96, 45, 35, 77]
def Largest(nums):
    largest = nums[0]
    n = len(nums)
    for i in range(0,n):
        if nums[i] > largest:
            largest = nums[i]
    return largest

print(Largest(nums))