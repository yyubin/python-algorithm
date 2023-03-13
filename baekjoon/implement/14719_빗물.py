import sys
h, w = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

result = 0
for i in range(1, w-1):
    left = max(li[:i])
    right = max(li[i+1:])

    compare = min(left, right)
    if li[i] < compare:
        result += compare - li[i]

print(result)

