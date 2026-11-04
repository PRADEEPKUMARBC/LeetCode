nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

n = len(nums)
max_sum = 0
for i in range(0, n):
    for j in range(i + 1, n):
        if nums[i] + nums[j] == max_sum:
            max_sum = nums[i] + nums[j]

print(max_sum)

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
def FindTheMaximumSubArray(nums):
    n = len(nums)
    maxi = float("-Inf")
    total = 0
    for i in range(0,n):
        total = total + nums[i]
        maxi = max(maxi, total)
        if total < 0:
            total = 0
    return maxi

print(FindTheMaximumSubArray(nums))
