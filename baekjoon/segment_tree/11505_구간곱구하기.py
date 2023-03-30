import sys
import math


def init(start, end, index):
    if start == end:
        tree[index] = arr[start]
    else:
        mid = (start + end) // 2
        tree[index] = init(start, mid, 2 * index) * init(mid + 1, end, 2 * index + 1) % 1000000007
    return tree[index]


def sub_mul(start, end, index, left, right):
    if left > end or right < start:
        return 1
    if left <= start and end <= right:
        return tree[index]

    mid = (start + end) // 2
    return sub_mul(start, mid, 2 * index, left, right) * sub_mul(mid + 1, end, 2 * index + 1, left,
                                                                   right) % 1000000007


def update_tree(start, end, index, where, diff):
    if where < start or end < where:
        return

    if start == end:
        tree[index] = diff
    else:
        mid = (start + end) // 2
        update_tree(start, mid, index * 2, where, diff)
        update_tree(mid + 1, end, index * 2 + 1, where, diff)
        tree[index] = tree[2 * index] * tree[2 * index + 1] % 1000000007


n, m, k = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(n)]
tree = [0] * (1 << (int(math.ceil(math.log2(n))) + 1))
init(0, n - 1, 1)

for _ in range(m + k):
    a, b, c = map(int, sys.stdin.readline().split())

    if a == 1:
        update_tree(0, n - 1, 1, b - 1, c)

    else:
        print(sub_mul(0, n - 1, 1, b - 1, c - 1))