n = int(input())

array = [int(x) for x in input().split()]

swaps = []

for i in range(n):
    minimum = i
    for j in range(i+1, n):
        if array[j] < array[minimum]:
            minimum = j
    
    if i != minimum:
        array[i], array[minimum] = array[minimum], array[i]
        swaps.append((i, minimum))

print(len(swaps))
for swap in swaps:
    print(f"{swap[0]} {swap[1]}")