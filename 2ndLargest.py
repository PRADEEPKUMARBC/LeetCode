# nums = [55, 32, 97, -55, 45, 32, 88, 21]

# n = len(nums)
# for i in range(0, n):
#     for j in range(i + 1, n):
#         if nums[i] > nums[j]:
#             nums[i], nums[j] = nums[j], nums[i]

# print(nums)
# print(nums[n - 2])


nums = [55, 32, 97, -55, 45, 32, 88, 21]

largest = float("-Inf") 
s_largest = float("-Inf") 
n = len(nums)
for i in range(0,n):
    if nums[i] > largest:
        s_largest = largest
        largest = nums[i]
    elif nums[i] > s_largest and nums[i] != largest:
        s_largest = nums[i]

print(s_largest)