import sys
n = int(sys.stdin.readline())
li = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    li.append((x, y))

li.sort()

start = li[0][0]
end = li[0][1]
ans = 0

for i in range(1, n):
    now_s, now_e = li[i]
    if now_s <= end:
        end = max(end, now_e)

    else:
        ans += (end - start)
        start = now_s
        end = now_e

ans += (end - start)
print(ans)


