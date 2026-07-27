# nums = [3,9,5,6,7,2]
# k = 3
# n = len(nums)
# rotations = k % n
# for  _ in range(0, rotations):
#     last = nums.pop()
#     first = nums.insert(0,last)

# print(nums)

# nums = [3, 9, 5, 6, 7, 2, 10, 9]
# k = 5
# n = len(nums)
# k = n % k

# nums[:] = nums[n-k:] + nums[:n-k]
# print(nums)

nums = [3, 9, 5, 6, 7, 2, 10, 9]
k = 5
n = len(nums)
def reverse(nums, left, right):
    while left< right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

reverse(nums, n-k, n-1) # reverse the last k elements
reverse(nums, 0, n-k-1) # reverse first n-k elements
reverse(nums, 0, n-1) # reverse whole array

print(nums)