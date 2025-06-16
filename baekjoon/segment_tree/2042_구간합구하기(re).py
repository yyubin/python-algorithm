import sys
n, m, k = map(int, sys.stdin.readline().split())
a = [int(sys.stdin.readline()) for _ in range(n)]
tree = [0] * (n*4)

def build(node, start, end):
    if start == end:
        tree[node] = a[start]
    else:
        mid = (start + end) // 2
        build(2*node, start, mid)
        build(2*node+1, mid+1, end)
        tree[node] = tree[2*node] + tree[2*node+1]

def query(node, start, end, left, right):
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    l_sum = query(2*node, start, mid, left, right)
    r_sum = query(2*node+1, mid+1, end, left, right)
    return l_sum + r_sum

def update(node, start, end, index, new):
    if start == end:
        tree[node] = new
    else:
        mid = (start + end) // 2
        if index <= mid:
            update(2*node, start, mid, index, new)
        else:
            update(2*node+1, mid+1, end, index, new)
        tree[node] = tree[2*node] + tree[2*node+1]

build(1, 0, n-1)
for _ in range(m+k):
    a_, b, c = map(int, sys.stdin.readline().split())
    if a_ == 1:
        a[b-1] = c
        update(1, 0, n-1, b-1, c)
    else:
        print(query(1, 0, n-1, b-1, c-1))
