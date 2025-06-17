import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
tree = [[0, 0] for _ in range(n*4)]

def build(node, start, end):
    if start == end:
        if a[start]%2 == 0:
            tree[node][0] = 1
        else:
            tree[node][1] = 1
    else:
        mid = (start + end) // 2
        build(node*2, start, mid)
        build(node*2+1, mid+1, end)
        tree[node] = [tree[node*2][0] + tree[node*2+1][0], tree[node*2][1] + tree[node*2+1][1]]

def update(node, start, end, index, val):
    if start == end:
        if val%2 == 0:
            tree[node] = [1, 0]
        else:
            tree[node] = [0, 1]
    else:
        mid = (start + end) // 2
        if index <= mid:
            update(node*2, start, mid, index, val)
        else:
            update(node*2+1, mid+1, end, index, val)
        tree[node] = [tree[node * 2][0] + tree[node * 2 + 1][0], tree[node * 2][1] + tree[node * 2 + 1][1]]

def query(node, start, end, left, right):
    if right < start or end < left:
        return [0, 0]
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    l = query(node*2, start, mid, left, right)
    r = query(node*2+1, mid+1, end, left, right)
    return [l[0] + r[0], l[1] + r[1]]

build(1, 0, n-1)
for _ in range(int(sys.stdin.readline())):
    a_, b, c = map(int, sys.stdin.readline().split())
    if a_ == 1:
        if a[b-1]%2 == c%2:
            a[b-1] = c
        else:
            update(1, 0, n-1, b-1, c)
            a[b-1] = c
    elif a_ == 2:
        print(query(1, 0, n-1, b-1, c-1)[0])
    else:
        print(query(1, 0, n-1, b-1, c-1)[1])

