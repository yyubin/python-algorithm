import sys
n = int(sys.stdin.readline())
li = []
d = [0] * n
d[0] = 1

for _ in range(n):
    li.append(int(sys.stdin.readline()))

max_ = 0
for i in range(1, n):
    for j in range(0, i):
        if li[j] < li[i]:
            max_ = max(max_, d[j])
    d[i] = max_ + 1
    max_ = 0


print(n - max(d))

#가장 긴 증가하는 부분수열 구해서 전체에서 빼주기
