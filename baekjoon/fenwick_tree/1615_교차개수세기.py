import sys
input = sys.stdin.read
n, m, *rest = map(int, input().split())
li = list(zip(rest[::2], rest[1::2]))

def update(tree, idx, val):
    while idx < len(tree):
        tree[idx] += val
        idx += idx & -idx

def query(tree, idx):
    result = 0
    while idx > 0:
        result += tree[idx]
        idx -= idx & -idx
    return result

li.sort()

tree = [0] * (n + 2)
inversion = 0
for i, j in li:
    inversion += query(tree, n) - query(tree, j)
    update(tree, j, 1)

print(inversion)


## 파이썬으론 안됨 cpp로 바꿔서 풀어야 할듯???