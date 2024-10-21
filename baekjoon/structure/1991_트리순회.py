import sys
n = int(sys.stdin.readline())
tree = {}

for _ in range(n):
    mid, left, right = map(str, sys.stdin.readline().split())
    tree[mid] = [left, right]

def pre(mid):
    if mid != '.':
        print(mid, end="")
        pre(tree[mid][0])
        pre(tree[mid][1])

def midd(mid):
    if mid != '.':
        midd(tree[mid][0])
        print(mid, end="")
        midd(tree[mid][1])

def post(mid):
    if mid != '.':
        post(tree[mid][0])
        post(tree[mid][1])
        print(mid, end="")


pre('A')
print()
midd('A')
print()
post('A')
