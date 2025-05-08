import sys
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        parent[y_root] = x_root

t = int(input())
for _ in range(t):
    n = int(sys.stdin.readline())
    coords = []
    for _ in range(n):
        x, y, r = map(int, sys.stdin.readline().split())
        coords.append((x, y, r))

    parent = list(range(n))

    for i in range(n):
        x1, y1, r1 = coords[i]
        for j in range(i+1, n):
            x2, y2, r2 = coords[j]
            dx = x1 - x2
            dy = y1 - y2
            dist_sq = (dx ** 2) + (dy ** 2)
            radius = r1 + r2
            if dist_sq <= radius ** 2:
                union(i, j)

    roots = set(find(i) for i in range(n))
    print(len(roots))

# 두 원의 중심 거리의 제곱이 두 반지름 합의 제곱보다 작거나 같으면 겹침 or 접함
# 걍 좌표평면이니까 제곱해서 비교
