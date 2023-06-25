import sys
n = int(sys.stdin.readline())
li = []

d, m = [0, 0, 0], [0, 0, 0]

for i in range(n):
    a, b, c = list(map(int, sys.stdin.readline().split()))
    d = [a + min(d[:2]), b + min(d), c + min(d[1:])]
    m = [a + max(m[:2]), b + max(m), c + max(m[1:])]

print(max(m), min(d))

# 메모리 초과
# for i in range(n):
#     d[i][0] = min(d[i-1][0], d[i-1][1]) + li[i][0]
#     d[i][1] = min(d[i-1][0], d[i-1][1], d[i-1][2]) + li[i][1]
#     d[i][2] = min(d[i-1][1], d[i-1][2]) + li[i][2]
#
#     m[i][0] = max(m[i-1][0], m[i-1][1]) + li[i][0]
#     m[i][1] = max(m[i-1][0], m[i-1][1], m[i-1][2]) + li[i][1]
#     m[i][2] = max(m[i-1][1], m[i-1][2]) + li[i][2]
#
# print(max(m[n-1][0], m[n-1][1], m[n-1][2]), end=" ")
# print(min(d[n-1][0], d[n-1][1], d[n-1][2]))








