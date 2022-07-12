t = int(input())

while t:
    t -= 1
    n = int(input())

    wheels = input().split()
    wheels = [int(x) for x in wheels]

    i = 0
    ans = []
    while i < n:
        line = input().split()
        to_move = int(line[0])
        movement = 0
        if to_move != 0:
            for ch in line[1]:
                if ch == 'U':
                    movement -= 1
                else:
                    movement += 1
            wheels[i] = (wheels[i] + movement)%10
        ans.append(str(wheels[i]))
        i += 1
    print(" ".join(ans))
