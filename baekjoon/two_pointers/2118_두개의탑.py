import sys
n = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for _ in range(n)]
prefix = [0] * (2*n+1)
for i in range(1, 2*n+1):
    prefix[i] = prefix[i-1] + li[(i-1)%n]

total = prefix[n]
half = total//2

res = 0
j = 0

for i in range(n):
    while j < i + n and prefix[j+1] - prefix[i] <= half:
        j += 1
    res = max(res, prefix[j] - prefix[i])

print(res)

# 여러 시점에서 슬라이딩 윈도우 or 투 포인터를 반복한다 → 누적합으로 최적화 가능할 가능성