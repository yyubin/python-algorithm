import sys
from itertools import permutations
n, k = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
res = 0
for comb in permutations(li, n):
    now = 500
    for i in comb:
        now += i
        now -= k
        if now < 500:
            break
    else:
        res += 1

print(res)

## 완전탐색

## dfs + 백트래킹
n, k = map(int, input().split())
kits = list(map(int, input().split()))

used = [False] * n
res = 0


def dfs(day, weight):
    global res
    if weight < 500:
        return  # 조기 가지치기
    if day == n:
        res += 1
        return

    for i in range(n):
        if not used[i]:
            used[i] = True
            dfs(day + 1, weight + kits[i] - k)
            used[i] = False  # 백트래킹


dfs(0, 500)
print(res)

