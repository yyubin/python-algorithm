import sys

n, m, b = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

result = sys.maxsize
level = 0

for i in range(257):
    use, get = 0, 0

    for x in range(n):
        for y in range(m):
            if graph[x][y] > i:
                get += graph[x][y] - i
            else:
                use += i - graph[x][y]

    if use > get + b:
        continue

    if get * 2 + use <= result:
        result = get * 2 + use
        level = i

print(result, level)

# dic 정렬
# li = sorted(dic.items(), key=lambda x: -x[1])
