# nums = [1,2,3,4,5,6,7,8,9]
# def sortedornot(nums):
#     n = len(nums)
#     for i in range(0, n):
#         for j in range(i + 1 , n):
#             if nums[i] > nums[j]:
#                 return False
#     return True

# print(sortedornot(nums))

nums = [7, 8, 62, 4, 6, 1, 3, 9]

def sortedornot(nums):
    n = len(nums)
    for i in range(0, n - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True

print(sortedornot(nums))