nums = [5, -2, 3, 9, 0, 6, 10, 7]

# k = 1
# for i in range(0, k):
#     Last = nums.pop()
#     nums.insert(0, Last)

# print(nums)

# k = 3
# n = len(nums)
# k = k % n

# for i in range(0, k):
#     front = nums.pop()
#     nums.insert(0,front)

# print(nums)

k = 3
n = len(nums)
k = n % k
nums = nums[n - k: ] + [] + nums[: n - k]
print(nums)