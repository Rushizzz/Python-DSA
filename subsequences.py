temp = [1,2,3,4]

all_subsets = []

k = 5

def backtrack(idx, curr_seq):
    #sum condition 
    if sum(curr_seq) == k:
        all_subsets.append(curr_seq[:])
        return 
    elif sum(curr_seq) > k:
        return

    #base case
    if idx >= len(temp):
        return 

    #include
    curr_seq.append(temp[idx])
    backtrack(idx+1,curr_seq)
    curr_seq.pop()

    #exclude
    backtrack(idx + 1, curr_seq)

    return

backtrack(0, [])

print(all_subsets)