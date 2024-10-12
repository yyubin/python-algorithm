# 자릿수가 n일경우
# 0으로 시작할 경우엔 안됨
# 큰수로 시작하는 것으로 찢기 시작하는게 유리

# 비트마스킹
# 2차원 배열을 일렬로 인덱스
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
#
# 1차원 인덱스로 변환
# 0 1 2 3
# 4 5 6 7
# 8 9 10 11
# 12 13 14 15
#
# 비트마스킹에서 1 << n*m 은 2의 n*m 제곱을 의미함
# 0001 에서 1 << 3 은 1000이고 이는 1이 8이됨을 의미 2의 n*m제곱이 됐음
#
# 그럼 총 2의 16제곱의 경우의 수가 있음 4x4기준 종이마다 잘리거나 잘리지않거나의 상태를 가짐 -> 2^16이고 비트마스킹으로는 1<<4*4
# 해당 idx로 찾아가기위해 2중for문 사용하고
# idx = row*m + col 이 해당 인덱스가 됨 (2차원배열을 1차원으로 늘린인덱스에서의 값..)
# 그 값이 지금 i에서? 1인지 아닌지 따져봐야함
# 애초에 그냥 부르트포스라서 모든 탐색을 하는 것
# 지금이 세로로 잘릴 차례면 세로로 자르고 가로로 잘릴 차례면 가로로 잘리는 것
# 만약 1 & (1<<idx) 가 1일경우 세로로 자른다고 가정,
# 1 & (1<<idx)가 0일경우 가로로 자름
# 그렇게 자르고? 잘린 부분 누적합으로 더해주고?
# 가장 큰값 리턴하면 된다
# 솔직히 비트마스킹해야겠다는 생각이 날지를 모르겠네

import sys
n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
result = 0

for bitmask in range(1 << (n * m)):
    total = 0

    for i in range(n):
        row_sum = 0
        for j in range(m):
            idx = i * m + j
            if bitmask & (1 << idx) != 0:
                row_sum = row_sum * 10 + graph[i][j]
            else:
                total += row_sum
                row_sum = 0
        total += row_sum

    for j in range(m):
        col_sum = 0
        for i in range(n):
            idx = i * m + j
            if (bitmask & (1 << idx)) == 0:
                col_sum = col_sum * 10 + graph[i][j]
            else:
                total += col_sum
                col_sum = 0
        total += col_sum

    result = max(result, total)

print(result)

