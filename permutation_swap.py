nums = [1,2,3]

n = len(nums)
result = []

def permutation_swap(idx):
    if idx == n - 1:
        result.append(nums[:])
        return 
    
    for i in range(idx, n):
        nums[i], nums[idx] = nums[idx], nums[i]
        permutation_swap(idx + 1)
        nums[i], nums[idx] = nums[idx], nums[i]
    

permutation_swap(0)
print(result)
