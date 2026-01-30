
nums = [4,5,7,7]
str_num = nums
global result
result = [0]
k = 2


def make_str(nums):
    str_nums = ""
    for i in nums:
        str_nums += str(i)
    return int(str_nums)

def solve(k, start):
    if k == 0 or start == len(nums) - 1:
        return 

    for i in range(start + 1, len(nums)):
        if str_num[start] < str_num[i] and str_num[i] == max(str_num[i:]):
            str_num[start], str_num[i] = str_num[i], str_num[start]
            result[0] = max( make_str(str_num), result[0])
            solve(k - 1, start + 1)
            str_num[start], nums[i] = nums[i], str_num[start]

solve(k, 0)
print(result)


