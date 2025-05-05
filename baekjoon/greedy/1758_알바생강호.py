import sys
n = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for _ in range(n)]
li.sort(reverse=True)
res = 0
for i in range(n):
    res += li[i] - i if li[i] - i >= 0 else 0
print(res)
