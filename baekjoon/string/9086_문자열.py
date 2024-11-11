import sys
for _ in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().rstrip()
    print(s[0], s[-1], sep="")