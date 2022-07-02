number = int(input())
skills = [int(x) for x in input().split()]

math = []
pe = []
prog = []

for i in range(number):
    if skills[i] == 1:
        prog.append(i+1)
    elif skills[i] == 2:
        math.append(i+1)
    else:
        pe.append(i+1)

x = min(len(math), len(pe), len(prog))
print(x)

for i in range(x):
    print(f"{math[i]} {pe[i]} {prog[i]}")