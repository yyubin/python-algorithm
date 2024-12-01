import sys
n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = [[0 for _ in range(n)] for _ in range(n)]
for k in range(5):
    for i in range(n):
        for j in range(n):
            if graph[i][k] == graph[j][k]:
                ans[i][j] = 1
                ans[j][i] = 1
tmp = []
for i in ans:
    tmp.append(i.count(1))
print(tmp.index(max(tmp))+1)

# 같은학생과 같은반 여러번일 경우 카운트 1이어ㅑㅇ함