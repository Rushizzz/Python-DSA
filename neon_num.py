number = int(input("enter your number\n"))

def neon(num):
    sqr = num * num
    addition = 0
    for i in str(sqr):
        addition += int(i)
    print(addition)
    return num == addition

print(neon(number))

