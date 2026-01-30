test_cases = [ 
    [4,5,2,10,8],
    [1,2,3,4],
    [9, 7, 5, 3],
    [2, 2, 2],
    [2, 2, 3, 1, 1, 5]
]
def next_greater_elements(nums):
    result = []
    i = 0
    j = i + 1
    while i < len(nums)+1:
        if j < len(nums):
            if nums[i] < nums[j]:
                result.append(nums[j])
                i += 1
                j = i + 1
            else:
                j += 1
                if j == len(nums):
                    result.append(-1)
                    i += 1
                    j = i + 1
        else:
            i += 1
    if len(result) != len(nums):
            extra = len(nums) - len(result)
            result.extend([-1]*extra)
    return result

for case in test_cases:
    print(f"Input: {case} => Output: {next_greater_elements(case)}")


