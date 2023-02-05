import sys

n = int(sys.stdin.readline())
li = []

for _ in range(n):
    n, m = map(int, sys.stdin.readline().split())
    li.append([n, m])


for i in li:
    rank = 1
    for j in li:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=" ")



