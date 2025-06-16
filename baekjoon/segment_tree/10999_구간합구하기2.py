import sys
n, m, k = map(int, sys.stdin.readline().split())
a = [int(sys.stdin.readline()) for _ in range(n)]
tree = [0] * (4*n)
lazy = [0] * (4*n)

def build(node, start, end):
    if start == end:
        tree[node] = a[start]
    else:
        mid = (start + end) // 2
        build(2*node, start, mid)
        build(2*node+1, mid+1, end)
        tree[node] = tree[2*node] + tree[2*node+1]

def propagate(node, start, end):
    if lazy[node] != 0:
        tree[node] += (end - start + 1) * lazy[node]
        if start != end:
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]
        lazy[node] = 0

def update(node, start, end, l, r, val):
    propagate(node, start, end)
    if r < start or end < l:
        return
    if l <= start and end <= r:
        tree[node] += (end - start + 1) * val
        if start != end:
            lazy[node*2] += val
            lazy[node*2+1] += val
        return
    mid = (start + end) // 2
    update(2*node, start, mid, l, r, val)
    update(2*node+1, mid+1, end, l, r, val)
    tree[node] = tree[2*node] + tree[2*node+1]

def query(node, start, end, left, right):
    propagate(node, start, end)
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    l_sum = query(2*node, start, mid, left, right)
    r_sum = query(2*node+1, mid+1, end, left, right)
    return l_sum + r_sum

build(1, 0, n-1)

for _ in range(m+k):
    x = list(map(int, sys.stdin.readline().split()))
    if x[0] == 1:
        update(1, 0, n-1, x[1]-1, x[2]-1, x[3])
    else:
        print(query(1, 0, n-1, x[1]-1, x[2]-1))

