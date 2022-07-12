t = int(input())
mem = {0:0}

def sumof2050(num):
    if num in mem:
        return mem[num]
    if num < 2050:
        return -1

    largest = 2050
    while largest*10 <= num:
        largest = largest* 10

    ans = sumof2050(num - largest)
    
    if ans == -1:
        mem[num] = -1
        return -1
    
    mem[num] = 1 + ans
    return 1 + ans

while t:
    t -= 1
    num = int(input())

    print(sumof2050(num))