import sys
n, m = map(int, sys.stdin.readline().split())
a = [0 for i in range(n)]
tree = [0] * (n*4)

def update(node, start, end, index, val):
    if start == end:
        tree[node] = val
    else:
        mid = (start + end) // 2
        if index <= mid:
            update(node*2, start, mid, index, val)
        else:
            update(node*2+1, mid+1, end, index, val)
        tree[node] = tree[node*2] + tree[node*2+1]

def query(node, start, end, left, right):
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    l_sum = query(node*2, start, mid, left, right)
    r_sum = query(node*2+1, mid+1, end, left, right)
    return l_sum + r_sum


for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    if x == 0:
        if y > z:
            y, z = z, y
        print(query(1, 0, n-1, y-1, z-1))
    else:
        a[y-1] = z
        update(1, 0, n-1, y-1, z)

# if y > z:
#     y, z = z, y
# 이 조건 빼먹고 풀었음
#