def combinationSum(candidates, target):
        ans, sol = [], []
        n = len(candidates)
        def backtrack(i, cur_sum):
            if cur_sum == target:
                ans.append(sol[:])
                return 
            
            if cur_sum > target or i == n:
                return
            
            backtrack(i+1, cur_sum)

            sol.append(candidates[i])
            backtrack( i, cur_sum + candidates[i] )
            sol.pop()

        backtrack(0, 0)
        return ans

nums = [1,2,3]
target = 5
print(combinationSum(nums, target))