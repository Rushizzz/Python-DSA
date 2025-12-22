# Python DSA permutation string program

question_str = "abc"
n = len(question_str)
ans = []

def permutation(curr):
    if len(curr) == n:
        ans.append(curr)
        return
    
    for i in question_str:
        if i not in curr:
            curr += i 
            permutation(curr)
            curr = curr[:-1]

permutation("")
print(ans)

