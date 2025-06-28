import sys
for _ in range(int(sys.stdin.readline())):
    n, k = map(int, sys.stdin.readline().split())
    li = [i+1 for i in range(n)]
    li.sort(reverse=True)

    if n - k == 1:
        li.sort()
        print(*li)
        continue

    for i in range(k):
        li.insert(i+1, li.pop())

    print(*li)