import sys
n, k = map(int, sys.stdin.readline().split())
li = sys.stdin.readline().rstrip()
visited = [False] * n

for i in range(n):
    if li[i] == 'P':
        for j in range(i-k, i+k+1):
            if 0 <= j < n and not visited[j] and li[j] == 'H':
                visited[j] = True
                break

print(visited.count(True))
