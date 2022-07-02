n = int(input())

managers = []
for _ in range(n):
    managers.append(int(input()))

max_len = 0

for i in range(n):
    len = 0
    p = managers[i]
    while p != -1:
        p = managers[p-1]
        len += 1
    if len > max_len:
        max_len = len

if n!= 0:
    print(max_len + 1)
else:
    print(0)