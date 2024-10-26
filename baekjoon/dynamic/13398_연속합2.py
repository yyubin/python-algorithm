import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
d = [[i for i in li] for _ in range(2)]

for i in range(1, n):
    d[0][i] = max(d[0][i-1] + li[i], d[0][i])
    d[1][i] = max(d[0][i-1], d[1][i-1] + li[i])

print(max(max(d[0]), max(d[1])))


# 상태가 2개 이상일 경우
# n차원 배열로 만들어볼 생각을 하자..
