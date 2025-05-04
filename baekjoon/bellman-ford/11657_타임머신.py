import sys
n, m = map(int, sys.stdin.readline().split())
edges = []
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    edges.append((a, b, c))
distance = [sys.maxsize] * (n + 1)
def bf(start):
    global n, m
    distance[start] = 0

    for i in range(n):
        for j in range(m):
            cur = edges[j][0]
            next = edges[j][1]
            cost = edges[j][2]

            if distance[cur] != sys.maxsize and distance[next] > distance[cur] + cost:
                distance[next] = distance[cur] + cost
                if i == n-1:
                    return True
    return False

cycle = bf(1)

if cycle:
    print("-1")
else:
    for i in range(2, n+1):
        if distance[i] == sys.maxsize:
            print("-1")
        else:
            print(distance[i])

# 벨만포드
# 시간복잡도 O(nm)
