# 2644번 : 촌수계산
from collections import deque
import sys

input = sys.stdin.readline
person = int(input())
a, b = map(int, input().split())
num = int(input())

visited = [False] * (person + 1)
graph = [[] for _ in range(person + 1)]
result = [0 for _ in range(person + 1)]

for _ in range(num):
    c, d = map(int, input().split())
    graph[c].append(d)
    graph[d].append(c)

for i in graph:
    i.sort()


def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                result[i] = v
                visited[i] = True



bfs(a)

cnt = 1
while True:
    if result[b] == 0:
        cnt = -1
        break
    if result[result[b]] == result[a]:
        break
    result[b] = result[result[b]]
    cnt += 1
print(cnt)

