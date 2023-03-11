import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
visited = [-1] * 100001
d = [-1] * 100001

def move(a):
    data = []
    temp = a
    for _ in range(visited[a] + 1):
        data.append(temp)
        temp = d[temp]
    print(' '.join(map(str, data[::-1])))

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 0
    while q:
        a = q.popleft()
        if a == k:
            print(visited[a])
            move(a)
            return
        for i in [a*2, a+1, a-1]:
            if 0 <= i < 100001:
                if visited[i] == -1 or visited[i] >= visited[a] + 1:
                    visited[i] = visited[a] + 1
                    q.append(i)
                    d[i] = a

bfs(n)



