import sys

n, k = map(int, sys.stdin.readline().split())
li = []
for _ in range(n):
    li.append(int(sys.stdin.readline().rstrip()))

i = len(li) - 1
cnt = 0
while k != 0 and i > -1:
    if k >= li[i]:
        a, b = divmod(k, li[i])
        cnt += a
        k = b
    i -= 1

print(cnt)
