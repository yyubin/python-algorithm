import sys
from bisect import bisect_left
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().rstrip().split()))

LIS = [a[0]]
record = []
result = []

for i in a:
    if LIS[-1] < i:
        LIS.append(i)
        record.append((len(LIS)-1, i))
    else:
        idx = bisect_left(LIS, i)
        LIS[idx] = i
        record.append((idx, i))

print(len(LIS))

location = len(LIS)-1
for i in range(n-1, -1, -1):
    if record[i][0] == location:
        result.append(record[i][1])
        location -= 1
    if location == -1:
        break

print(*reversed(result))
