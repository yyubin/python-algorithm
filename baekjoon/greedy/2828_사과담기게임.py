import sys
n, m = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())
apples = [int(sys.stdin.readline()) for _ in range(t)]
res = 0
now = (1, m)
for i in range(t):
    move = 0
    if apples[i] > now[1]:
        move = apples[i] - now[1]
        now = (now[0] + move, now[1] + move)
    elif apples[i] < now[0]:
        move = now[0] - apples[i]
        now = (now[0] - move, now[1] - move)
    res += move
print(res)

# 시간복잡도 O(t)