import sys
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    minus = [a[i] - b[i] for i in range(n)]
    max_ = max(minus)
    minus = [minus[i] if b[i] > 0 else max_ for i in range(n)]
    now = minus[0]
    for i in minus:
        if i != now or i < 0:
            print("NO")
            break
    else:
        print("YES")
