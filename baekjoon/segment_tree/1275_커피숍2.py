import sys

def init(start, end, index):
    if start == end:
        tree[index] = li[start]
        return tree[index]
    mid = (start + end) // 2
    tree[index] = init(start, mid, index * 2) + init(mid + 1, end, index * 2 + 1)
    return tree[index]

def interval_sum(start, end, index, left, right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return tree[index]
    mid = (start + end) // 2
    return interval_sum(start, mid, index * 2, left, right) + interval_sum(mid + 1, end, index * 2 + 1, left, right)

def update(start, end, index, what, value):
    if what < start or what > end:
        return
    tree[index] += value
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, index * 2, what, value)
    update(mid + 1, end, index * 2 + 1, what, value)

n, q = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
tree = [0] * 4 * n

init(0, n - 1, 1)
for _ in range(q):
    x, y, a, b = map(int, sys.stdin.readline().split())
    if y < x:
        x, y = y, x
    print(interval_sum(0, n - 1, 1, x - 1, y - 1))
    update(0, n - 1, 1, a - 1, b - li[a - 1])
    li[a - 1] = b
