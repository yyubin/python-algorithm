import sys
r, c = map(int, sys.stdin.readline().split())
graph = []

for _ in range(r):
    graph.append(list(sys.stdin.readline().rstrip()))

visited = [[-1] * c for _ in range(r)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
alphabet = set()

def dfs(x, y, cnt):
    global result

    result = max(result, cnt)
    alphabet.add(graph[x][y])
    for k in range(4):
        ddx = dx[k] + x
        ddy = dy[k] + y
        if 0 <= ddx < r and 0 <= ddy < c and graph[ddx][ddy] not in alphabet:
            dfs(ddx, ddy, cnt + 1)
    #고른 길이 최대길이 아닐수도 있으니 돌아갈 수 있게 하기
    alphabet.remove(graph[x][y])


result = 0
dfs(0, 0, 1)
print(result)

## bfs로도 풀릴듯
# 시간초과나서 alphabet을 list에서 set으로 바꿈
