import sys
input = sys.stdin.readline
results = []
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    fix = set()
    for i in range(n):
        if b[i] != -1:
            fix.add(a[i] + b[i])

    if len(fix) == 1:
        x = next(iter(fix))
        ok = True
        for i in range(n):
            if b[i] == -1:
                val = x - a[i]
                if not (0 <= val <= k):
                    ok = False
                    break
            elif a[i] + b[i] != x:
                ok = False
                break
        results.append("1" if ok else "0")

    elif len(fix) == 0:
        a.sort()
        results.append(str(max(0, (a[0] + k) - a[-1] + 1)))

    else:
        results.append("0")

sys.stdout.write("\n".join(results) + "\n")

# 시간초과로 cpp로 제출