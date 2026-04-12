import sys
r, c = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline()) for _ in range(r)]

for i in range(r):
    for j in range(c):
        if graph[i][j] == '.':
            tmp = 0
            if i != 0:
                tmp += 1 if graph[i - 1][j] == '.' else 0
            if i != r - 1:
                tmp += 1 if graph[i + 1][j] == '.' else 0
            if j != 0:
                tmp += 1 if graph[i][j - 1] == '.' else 0
            if j != c - 1:
                tmp += 1 if graph[i][j + 1] == '.' else 0

            if tmp < 2:
                print(1)
                sys.exit()

print(0)