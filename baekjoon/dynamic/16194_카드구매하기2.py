import sys
n = int(sys.stdin.readline())
p = [0] + list(map(int, sys.stdin.readline().split()))

d = [0] * (n+1)
d[1] = p[1]
d[2] = min(p[1]*2, p[2])

for i in range(3, n+1):
    d[i] = p[i]
    for j in range(1, i//2+1):
        d[i] = min(d[i], d[j] + d[i-j])

print(d[-1])


# d[n] 은 카드를 n개 사는 경우


# d[0] = 0
# d[1] = p[1]
# print(p)
# for i in range(2, len(p)):
#     print(d)
#     d[i] = min((n // i) * p[i] + d[n % i], ((n // i) + 1) * p[i])
#
# print(d)
# print(d[-1])

