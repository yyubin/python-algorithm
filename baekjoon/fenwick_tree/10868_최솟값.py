import sys

MAX = sys.maxsize
n, m = map(int, sys.stdin.readline().split())
arr = [0]
tree = [MAX] * (n + 1)
tree2 = [MAX] * (n + 1)

for _ in range(n):
    arr.append(int(sys.stdin.readline()))


def update(i, target):
    while i <= n:
        tree[i] = min(tree[i], target)
        i += (i & -i)


def update2(i, target):
    while 0 < i:
        tree2[i] = min(tree2[i], target)
        i -= (i & -i)


def find(start, end):
    result = MAX

    prev = start
    curr = prev + (prev & -prev)
    while curr <= end:
        result = min(result, tree2[prev])
        prev = curr
        curr = prev + (prev & -prev)
    result = min(result, arr[prev])

    prev = end
    curr = prev - (prev & -prev)
    while curr >= start:
        result = min(result, tree[prev])
        prev = curr
        curr = prev - (prev & -prev)

    return result


for i, x in enumerate(arr):
    if i > 0:
        update(i, x)
        update2(i, x)

for _ in range(m):
    start, end = map(int, input().split())
    print(find(start, end))

# 펜윅트리
#https://thinkmath2020.tistory.com/709
# & 연산자 (비트 연산자)
# https://codechacha.com/ko/python-difference-and-ampersand/