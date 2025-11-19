import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))

    C = n + 1
    q = [C - x for x in p]
    print(*q)
