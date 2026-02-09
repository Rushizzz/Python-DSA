# Python DSA permutation program

nums = [1,2,3]
n = len(nums)
ans = []
curr = []
def permutation(curr):
    if len(curr) == n:
        ans.append(curr.copy())
        return
    
    for i in nums:
        if i not in curr:
            curr.append(i) 
            permutation(curr)
            curr.pop()

permutation(curr)
print(ans)
