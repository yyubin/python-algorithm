for tc in range(1, int(input())+1):
    n = int(input())
    d = [0] * (n+10)

    # 2x 2x+1
    d[0] = 1
    d[1] = 1 # 1, (2, 3)
    d[2] = 1 # 1, (2, 3)
    d[3] = 2 # 1, (2)   2, (4, 5)
    d[4] = 2 # 1, (2)   2, (4, 5)
    d[5] = 2 # 1, (2)   2, (4, 5)
    d[6] = 2 # 1, (3)   3, (6, 7)
    d[7] = 3 # 1, (3)   3, (6)  6, (12, 13)


    for i in range(8, n+1):
        d[i] = min(d[i%2]+1, d[(i-1%2)]+1)

    print(d[n])

#메모리초과