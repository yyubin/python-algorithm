import sys
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    li = list(sys.stdin.readline().rstrip())
    cnt = 0
    s = set()

    for i in li:
        if i not in s:
            if ord(i) - 64 <= li.count(i):
                cnt += 1
            s.add(i)
    print(cnt)