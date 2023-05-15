import sys
from collections import deque

num1, num2 = map(int, input().split())
graph = []

for i in range(num1):
    g = list(map(int, input().rstrip()))
    graph.append(g)

visited = [[False] * num2 for _ in range(num1)]

def bfs(start):
    q = deque([start])
    visited[start] = True


