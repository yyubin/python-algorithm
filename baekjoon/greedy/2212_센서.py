import sys
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
li.sort()
dist = []
if k >= n:
    print(0)
    sys.exit()

for i in range(n-1):
    dist.append(li[i+1] - li[i])

dist.sort()
for i in range(k-1):
    dist.pop()

print(sum(dist))

# 그리디 + 거리차이 최소합
# 집중국이 커버하는 범위는 센서들로부터 시작해서 끊을 수 있는 간격
# 센서 좌표를 오름차순 정렬하고, 인접한 센서 간 거리 차이를 구해보면
# 센서:     s1    s2    s3     s4
# 거리차:     d1    d2     d3
# 가장 멀리 떨어진 거리차를 끊어주면, 그만큼 총 길이를 줄일 수 있음
# 따라서 → 간격 중 가장 큰 것부터 (K-1)개를 끊는다.
