t = int(input())

while t:
    t -= 1

    n = int(input())
    string = list(input())
    solved = set(string)

    print(len(string) + len(solved))