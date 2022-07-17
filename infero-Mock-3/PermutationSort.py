t = int(input())

while t:
    t -= 1
    n, m = map(int, input().split())

    a = [int(x) for x in input().split()]
    p = [int(x)-1 for x in input().split()]
    p = set(p)

    flag = 1
    for i in range(len(a)):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                if j not in p:
                    flag = 0
                    break
                else:
                    a[j], a[j+1] = a[j+1], a[j]

    if flag:
        print("YES")
    else:
        print("NO")