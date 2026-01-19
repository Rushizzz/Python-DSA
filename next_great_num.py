test_cases = [
    [1,2,3,4],
    [4,5,2,10,8],
    [9,7,5,3],
    [2,2,2],
    [2,2,3,1,1,5]
]

def next_great_number(nums):
    if len(nums) <= 1:
        return -1

    i = 0
    j = 1
    while i < len(nums):
        if j < len(nums) and nums[i] < nums[j]:
            nums[i] = nums[j]
            i += 1
            j = i + 1
        else:
            if j < len(nums):
                j += 1
            else:
                nums[i] = -1
                i += 1
                j = i + 1
    return nums

for case in test_cases:
    print(next_great_number(case))
# Expected outputs:
# [2, 3, 4, -1]
# [5, 10, 10, -1, -1]
# [-1, -1, -1, -1]
# [-1, -1, -1]
# [3, 3, 5, 5, 5, -1]

