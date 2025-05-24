import sys
n, s = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
cnt = 0
ans = []

def solve(x):
    global cnt
    if sum(ans) == s and len(ans) > 0:
        cnt += 1

    for i in range(x, n):
        ans.append(li[i])
        solve(i+1)
        ans.pop()

solve(0)
print(cnt)