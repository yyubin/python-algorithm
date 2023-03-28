import sys
n, m = map(int, sys.stdin.readline().split())
li = [int(sys.stdin.readline()) for _ in range(n)]
tree = [[1000000000, 1] for _ in range(4 * n)]

def init(start, end, index):
    if start == end:
        tree[index] = [li[start], li[start]]
        return tree[index]

    mid = (start+end) // 2
    l, r = init(start, mid, index*2), init(mid+1, end, index*2+1)
    tree[index] = [min(l[0], r[0]), max(l[1], r[1])]
    return tree[index]

def interval_minmax(start, end, index, left, right):
    if left > end or right < start:
        return [1000000000, 0]

    if left <= start and right >= end:
        return tree[index]

    mid = (start+end) // 2
    l, r = interval_minmax(start, mid, index * 2, left, right), interval_minmax(mid + 1, end, index * 2 + 1, left, right)
    return [min(l[0], r[0]), max(l[1], r[1])]

init(0, n-1, 1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(*interval_minmax(0, n-1, 1, a-1, b-1))
