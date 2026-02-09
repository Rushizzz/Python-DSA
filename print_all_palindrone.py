def check_if_palindrone(substring):
    i,j = 0,len(substring) - 1
    while i != j:
        if substring[i] != substring[j]:
            return False
        else:
            i += 1
            j -= 1
    return True


substring = "aaba"

ans = check_if_palindrone(substring)
print(ans)