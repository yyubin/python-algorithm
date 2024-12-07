import sys
from collections import deque
d = deque()
for _ in range(int(sys.stdin.readline())):
    i = list(map(int, sys.stdin.readline().split()))

    if i[0] == 1:
        d.insert(0, i[1])
    elif i[0] == 2:
        d.append(i[1])
    elif i[0] == 3:
        if len(d) > 0:
            print(d.popleft())
        else:
            print(-1)
    elif i[0] == 4:
        if len(d) > 0:
            print(d.pop())
        else:
            print(-1)
    elif i[0] == 5:
        print(len(d))
    elif i[0] == 6:
        if len(d) > 0:
            print(0)
        else:
            print(1)
    elif i[0] == 7:
        if len(d) > 0:
            print(d[0])
        else:
            print(-1)
    else:
        if len(d) > 0:
            print(d[-1])
        else:
            print(-1)
