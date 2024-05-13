import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
li.sort()

result = 0
for i in range(n//2):
    result += abs(li[i] - li[n//2+1])

print(result)
