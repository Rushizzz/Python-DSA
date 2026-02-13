def check_if_palindrome(substring):
    i,j = 0,len(substring) - 1
    while i < j:
        if substring[i] != substring[j]:
            return False
        i += 1
        j -= 1
    return True

def solve(index, substring, current_partition, result):
    if index == len(substring):
        result.append(current_partition.copy())
    temp_string = ''
    for i in range(index, len(substring)):
        temp_string += substring[i]
        if check_if_palindrome(temp_string):
            current_partition.append(temp_string)
            solve(i+1, substring, current_partition, result)
            current_partition.pop()

index, current_partition, result = 0, [], []

substring = 'aaab'
solve(index, substring, current_partition, result)
print(result)
