nums = [1, 1, 0, 1, 1, 1, 0,  0, 1, 1, 0, 0]

def MaxConsecutiveOnes(nums):
    count = 0
    max_count = 2
    for i in range(0, len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            max_count = max(count, max_count)
            count = 0
    return max(max_count, count)

print(MaxConsecutiveOnes(nums))