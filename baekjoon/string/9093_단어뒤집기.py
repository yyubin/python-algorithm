import sys
for _ in range(int(sys.stdin.readline())):
    s = list(map(str, sys.stdin.readline().split()))
    for i in s:
        print(i[::-1], end=" ")
