
def find_all_subsets(nums):
    all_subsets = []

    def backtrack(start, curr_subset):
        all_subsets.append(curr_subset[:])

        for i in range(start, len(nums)):
        
            curr_subset.append(nums[i])

            backtrack(i + 1, curr_subset)

            curr_subset.pop()
        
    backtrack(0, [])
    return all_subsets

print(
    find_all_subsets(
        [1,2,3]
    )
)