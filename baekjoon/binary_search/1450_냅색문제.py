import sys
from itertools import combinations
n, c = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
li1, li2 = li[:n//2], li[n//2:]
a, b = [], []

cnt = 1

for i in range(1, len(li1)+1):
    for j in combinations(li1, i):
        tmp = sum(j)
        if tmp <= c:
            a.append(tmp)

for i in range(1, len(li2)+1):
    for j in combinations(li2, i):
        tmp = sum(j)
        if tmp <= c:
            b.append(tmp)

b.sort()

for i in a:
    start, end = 0, len(b)
    while start < end:
        mid = (start + end)//2
        if i + b[mid] <= c:
            start = mid + 1
        else:
            end = mid

    cnt += end

print(cnt + len(a) + len(b))


## MITM
# 반으로 나눠서 조합으로 가능한 부분합을 각각 더해줌
# 서로 더해서 가능한지 판별(이분탐색)
# a의 길이, b의 길이, cnt의 합이 정담이 됨