import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
tree = [None] * (4 * n)

def build(node, start, end):
    if start == end:
        tree[node] = (a[start], start)
    else:
        mid = (start + end) // 2
        build(2*node, start, mid)
        build(2*node+1, mid+1, end)
        tree[node] = min(tree[node*2], tree[node*2+1])

def update(node, start, end, idx, value):
    if start == end:
        tree[node] = (value, idx)
    else:
        mid = (start + end) // 2
        if idx <= mid:
            update(2*node, start, mid, idx, value)
        else:
            update(2*node+1, mid+1, end, idx, value)
        tree[node] = min(tree[node*2], tree[node*2+1])

def query(node, start, end, l, r):
    if r < start or end < l:
        return (float('inf'), float('inf'))
    if l <= start and end <= r:
        return tree[node]
    mid = (start + end) // 2
    left = query(2*node, start, mid, l, r)
    right = query(2*node+1, mid+1, end, l, r)
    return min(left, right)

build(1, 0, n-1)
for _ in range(int(sys.stdin.readline())):
    x = list(map(int, sys.stdin.readline().split()))
    if x[0] == 1:
        update(1, 0, n-1, x[1]-1, x[2])
    else:
        print(query(1, 0, n-1, 0, n-1)[1] + 1)

# 세그먼트트리 안넣고 그냥 풀 수 있음(힙큐+맵)
import sys
import heapq
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
heap = []

for i in range(n):
    heapq.heappush(heap, (a[i], i))

for _ in range(int(input())):
    q = list(map(int, input().split()))
    if q[0] == 1:
        i = q[1] - 1
        a[i] = q[2]
        heapq.heappush(heap, (a[i], i))
    else:
        while True:
            val, idx = heap[0]
            if a[idx] == val:
                print(idx + 1)
                break
            else:
                heapq.heappop(heap)

# update 된 값도 무조건 힙에 넣고
# 꺼낼때만 제대로 된지 확인함
# 지연삭제

# import sys
# n = int(sys.stdin.readline())
# a = list(map(int, sys.stdin.readline().split()))
# tree = [0] * (4*n)
#
# def build(node, start, end):
#     if start == end:
#         tree[node] = a[start]
#     else:
#         mid = (start + end) // 2
#         build(2*node, start, mid)
#         build(2*node+1, mid+1, end)
#         tree[node] = tree[2*node] + tree[2*node+1]
#
# def update(node, start, end, index, new):
#     if start == end:
#         tree[node] = new
#     else:
#         mid = (start + end) // 2
#         if index <= mid:
#             update(2*node, start, mid, index, new)
#         else:
#             update(2*node+1, mid+1, end, index, new)
#         tree[node] = tree[2*node] + tree[2*node+1]
#
# def min_index_query(node, start, end, index):
#     if start == end:
#         if tree[node] < tree[index]:
#             return node
#         else:
#             return index
#     else:
#         mid = (start+end) // 2
#         if tree[2*node] <= tree[2*node+1]:
#             return min_index_query(2*node, start, mid, min(2*node, index))
#         else:
#             return min_index_query(2*node+1, mid+1, end, min(2*node+1, index))
#
#
# build(1, 0, n-1)
# for _ in range(int(sys.stdin.readline())):
#     x = list(map(int, sys.stdin.readline().split()))
#     if x[0] == 1:
#         a[x[1]-1] = x[2]
#         update(1, 0, n-1, x[1]-1, x[2])
#     else:
#         idx = min_index_query(1, 0, n - 1, sys.maxsize)
#         print(a.index(tree[idx])+1)
#
#
