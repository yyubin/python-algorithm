import sys
for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())

    if a%2 == 0:
        if b%2 == 1:
            print(-1)
        else:
            print(a*b+1)
            continue

    if b%2 == 0:
        if (b//2)%2 == 1:
            k = (b//2)
            print(a * k + (b//k))
        else:
            print(-1)
    else:
        print(a*b+1)

    # for i in range(b, 0, -1):
    #     if b%i == 0:
    #         tmp = (b//i) + (a*i)
    #         if tmp%2 == 0:
    #             print(tmp)
    #             break
    # else:
    #     print(-1)