import sys
li = [int(sys.stdin.readline()) for _ in range(10)]

for i in range(1, 10):
    li[i] += li[i-1]

ans = 0
for i in li:
    if abs(100-ans) > abs(100-i):
        ans = i
    elif abs(100-ans) == abs(100-i):
        ans = max(ans, i)

print(ans)
