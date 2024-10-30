import sys
n, c = map(int, sys.stdin.readline().split())
li = [int(sys.stdin.readline()) for _ in range(n)]
li.sort()

start = 1
end = li[-1] - li[0]
result = 0

while start <= end:
    mid = (start+end)//2
    now = li[0]
    cnt = 1

    for i in range(1, n):
        if li[i] >= now + mid:
            cnt += 1
            now = li[i]

    if cnt >= c:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)

# 공유기 거리는 최소 1, 공유기 거리 최대는 li[-1]-li[0]
# 1 2 4 8 9
# start = 1, end = 8
# "설치가능한공유기거리"를 구함, 기존 집들 방문하면서, 지금 설치가 가능한지 확인함
# 만약 설치 수가 목표하는 수보다 크면 공유기 사이의 거리를 늘리고
# 설치 수가 목표하는 수보다 작으면 공유기의 사이의 거리를 좁히면서 찾는것
# cnt가 c보다 크면 더 설치할 수 있으니 간격없 넓혀보고 아니면 간격을 줄이면서
# cnt가 c보다 작은 경우 그냥 c개의 공유기 설치가 불가능함
