import sys
n = int(sys.stdin.readline())
c = 0
t = 0
while True:
    c += 1
    if '666' in str(c):
        t += 1
    if t == n:
        print(c)
        break
