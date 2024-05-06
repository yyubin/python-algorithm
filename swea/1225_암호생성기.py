from collections import deque
for _ in range(10):
    tc = int(input())
    li = deque(list(map(int, input().split())))
    n = 1

    while True:
        x = li.popleft() - n
        if x <= 0:
            li.append(0)
            break
        li.append(x)
        n += 1
        if n == 6:
            n = 1

    print('#'+str(tc), *li)


