import sys
n, k = map(int, sys.stdin.readline().split())
tree = [[] for _ in range(n+1)]
tree[1] = [1]

for i in range(2, n+1):
    tmp = []
    for j in range(i):
        if j == 0 or j == i-1:
            tmp.append(1)
            if j == i-1:
                tree[i] = tmp
            continue
        tmp.append(tree[i-1][j-1] + tree[i-1][j])
        tree[i] = tmp
print(tree[n][k-1])
