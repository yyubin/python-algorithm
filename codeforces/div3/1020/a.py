import sys
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().rstrip()
    res = (s.count('1')) * n
    for i in range(n):
        if s[i] == '1':
            res -= 1
        else:
            res += 1
    print(res)

