import sys
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))

    for i in range(3):
        if i%2 == 0:
            idx = -1
            tmp = 0
            for i in range(n):
                if a[i] > 0 and b[i] > 0 and b[i] > tmp:
                    idx = i
                    tmp = b[i]
            if idx == -1:
                break
            a[idx] -= 1
            b[idx] = 0
        else:
            idx = -1
            tmp = 0
            for i in range(n):
                if b[i] > 0 and a[i] > tmp:
                    idx = i
                    tmp = a[i]
            if idx == -1:
                break
            b[idx] -= 1
            a[idx] = 0

    print(a)
    print(b)
    print(sum(a) - sum(b))

