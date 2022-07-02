n = input()

index = 0

for digit in n:
    if digit == '4':
        index = index*2 + 1
    else:
        index = index*2 + 2

print(index)