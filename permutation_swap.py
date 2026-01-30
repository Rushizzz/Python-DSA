
question = [1,2,3]
n = len(question)
result = []
def permutation_swap(idx):

    if idx == n-1:
        result.append(question[:])
        return 

    for i in range(idx,n):
        question[i], question[idx] = question[idx], question[i]
        permutation_swap(idx + 1)
        question[i], question[idx] = question[idx], question[i]

permutation_swap(0)
print(result)