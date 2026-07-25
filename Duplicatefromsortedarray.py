# arr = [1,1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]

# freq_map = {}
# n = len(arr)
# for i in range(0, n):
#     if arr[i] in freq_map:
#         freq_map[arr[i]] += 1
#     else:
#         freq_map[arr[i]] = 1

# print(freq_map)

def Duplicate(arr):
    n = len(arr)

    if n == 1:
        return 1
    i = 0
    j = i + 1

    while j < n:
        if arr[j] != arr[i]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1

    return arr[:i+1]
arr = [1,1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]

print(Duplicate(arr))