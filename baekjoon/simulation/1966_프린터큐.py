import sys

cnt = int(input())

while cnt > 0:
    n, m = map(int, sys.stdin.readline().split())
    li = list(map(int, sys.stdin.readline().split()))

    index = [i for i in range(n)]

    result_li = []
    index_li = []

    while len(li) != 0:
        if li[0] == max(li):
            result_li.append(li[0])
            index_li.append(index[0])
            li.pop(0)
            index.pop(0)

        else:
            li.append(li[0])
            li.pop(0)
            index.append(index[0])
            index.pop(0)

    print(index_li.index(m) + 1)

    cnt -= 1
