import sys
sys.setrecursionlimit(100000)

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
remove = int(sys.stdin.readline())

def dfs(idx):
    li[idx] = -2
    for i in range(n):
        if idx == li[i]:
            dfs(i)

dfs(remove)

result = 0
for i in range(n):
    if li[i] != -2 and i not in li:
        result += 1

print(result)



