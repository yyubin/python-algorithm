import sys
for _ in range(int(sys.stdin.readline())):
    n, k = map(int, sys.stdin.readline().split())
    paper = sys.stdin.readline().rstrip()

    res = paper[:k].count("W")
    now = res
    las = paper[0] == "W"
    for i in range(1, n-k+1):
        tmp = paper[i+(k-1)] == "W"
        las = paper[i-1] == "W"
        if tmp:
            now += 1
        if las:
            now -= 1

        res = min(now, res)
    print(res)

# 1:35:55