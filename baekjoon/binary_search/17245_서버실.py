import sys
n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

total = sum(sum(row) for row in graph)
if total == 0:
    print(0)
    sys.exit()

goal = (total + 1) // 2

def chk(x):
    return sum(min(graph[i][j], x) for i in range(n) for j in range(n))

left, right = 0, int(1e8)
ans = 0
while left <= right:
    mid = (left + right) // 2
    if chk(mid) < goal:
        left = mid + 1
    else:
        ans = mid
        right = mid - 1

print(int(ans))