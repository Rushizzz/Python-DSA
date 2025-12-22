
def sum_of_combinations(nums, k):
    all_sets = []
    def backtrack(idx, curr_list):
        if sum(curr_list) == k:
            all_sets.append(curr_list[:])
            return 
        elif sum(curr_list) > k:
            return
        
        if idx >= len(nums):
            return

        #exclude
        backtrack(idx+1, curr_list)

        #include
        curr_list.append(nums[idx])
        backtrack(idx+1, curr_list)

        #undo
        curr_list.pop()

        return 

    
    backtrack(0, [])
    print(all_sets)

nums = [1,2,3,4,5]
k = 6
sum_of_combinations(nums, k)


