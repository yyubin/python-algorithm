import sys
n = int(sys.stdin.readline())
balls = []

for i in range(n):
    color, size = map(int, sys.stdin.readline().split())
    balls.append((size, color, i))
balls.sort()

res = [0] * n
color_sum = [0] * (n+1)
total = 0
j = 0

for i in range(n):
    cur_size, cur_color, cur_i = balls[i]
    while balls[j][0] < cur_size:
        size_j, color_j, i_j = balls[j]
        total += size_j
        color_sum[color_j] += size_j
        j += 1
    res[cur_i] = total - color_sum[cur_color]

print(*res, sep="\n")

# 정렬 + 누적합 + 투포인터
# O(n log n) + O(n) + O(n) = O(n log n)
# 공 크기 기준으로 정렬
# 색별로 누적합
# 투 포인터 : 현재 공보다 작은 들의 크기 누적
# 내가 잡을 수 있는 공의 크기 = 전체 누적합 - 같은 색 누적합

# 조건 기반의 누적 합을 구할 때 정렬 후 누적합을 빼는 방식으로 구할 수 있을지 생각해보기
# 그리고 크기가 기준이 되는 지금같은 문제에선, 크기 기준으로 정렬을 해보고 생각해도 좋을 듯
# "크기, 길이, 거리, 시간" 같은 정렬 기준이 보이면 → 먼저 정렬하고 → 누적합이나 투포인터로 최적화할 수 없을까?