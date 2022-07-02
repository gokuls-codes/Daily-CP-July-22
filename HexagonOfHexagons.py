lst = [int(x) for x in input().split()]
lst.sort()

tmp = lst[0] - 1
ans = (lst[2] + tmp) * (lst[1] + tmp)


ans -= (tmp * (tmp+1))

print(ans)