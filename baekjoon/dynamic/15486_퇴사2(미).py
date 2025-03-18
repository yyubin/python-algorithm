import sys
cnt = int(sys.stdin.readline())
t = []
p = []

for _ in range(cnt):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    t.append(a)
    p.append(b)

d = [0] * (cnt + 1)

tmp = 0
for i in range(cnt):
    tmp = max(tmp, d[i])
    if i + t[i] > cnt:
        continue
    d[i+t[i]] = max(tmp + p[i], d[i + t[i]])


print(max(d))

# n이 150만이므로 O(N), O(N log N)까지 가능
# dp로 시간복잡도 O(N)

# d[i+t[i]] = max(tmp + p[i], d[i + t[i]])
# 현재까지 쌓인 최대 이익(tmp) + 이번 상담 이익(p[i])
# 이미 저장된 값(d[i+t[i]]) 중 더 큰 값으로 갱신