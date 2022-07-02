t = int(input())

while t > 0:
    t -= 1
    string = input()

    i = 0
    max_len = 0
    while i < len(string):
        length = 0
        while i < len(string) and string[i] == 'L':
            length += 1
            i += 1
        if length > max_len:
            max_len = length
        i += 1

    print(max_len + 1)