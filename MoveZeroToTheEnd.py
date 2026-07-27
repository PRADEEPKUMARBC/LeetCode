nums = [1, 0, 0, 3, 2, 4, 0, 5, 2, 0, 8, 0, 4]

n = len(nums)
temp = []
for i in range(0,n):
    if nums[i] != 0:
        temp.append(nums[i])

nz = len(temp)
for i in range(0, nz):
    nums[i] = temp[i]

for i in range(nz, n):
    nums[i] = 0

print(nums)