import sys

while True:
    li = list(map(int, sys.stdin.readline().split()))
    if sum(li) == 0:
        sys.exit()
    max_ = li.pop(li.index(max(li)))

    if max_**2 == li[0]**2 + li[1]**2:
        print("right")
    else:
        print("wrong")
