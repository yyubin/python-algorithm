import sys
sys.setrecursionlimit(10**6)

def hanoi(n, start, end, via, steps):
    if n == 1:
        steps.append((start, end))
        return
    hanoi(n-1, start, via, end, steps)
    steps.append((start, end))
    hanoi(n-1, via, end, start, steps)

n = int(sys.stdin.readline())
steps = []

if n <= 20:
    hanoi(n, 1, 3, 2, steps)
    print(len(steps))
    for a, b in steps:
        print(a, b)
else:
    print(2**n-1)
