import sys
n = int(sys.stdin.readline())
graph = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def seat_score(likes):
    global dx, dy
    tmp_graph = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] in likes:
                        tmp_graph[i][j] += 1

    seat_candidates = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                        cnt += 1
                seat_candidates.append((tmp_graph[i][j], i, j, cnt))

    seat_candidates.sort(key=lambda x: (-x[0], -x[3], x[1], x[2]))
    return seat_candidates

satis = [[0] * n for _ in range(n)]
stu = {}

for x in range(n ** 2):
    li = list(map(int, sys.stdin.readline().split()))
    stu[li[0]] = li[1:]
    candidates = seat_score(li[1:])
    graph[candidates[0][1]][candidates[0][2]] = li[0]
    visited[candidates[0][1]][candidates[0][2]] = True

for i in range(n):
    for j in range(n):
        for k in range(4):
            nx = dx[k] + i
            ny = dy[k] + j
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] in stu[graph[i][j]]:
                    satis[i][j] += 1

score_table = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000}
res = sum(score_table[j] for row in satis for j in row)

print(res)

# 시간 복잡도 O(N^2)
# I, J 탐색에 N^2 이고 4방향 탐색은 O(1)
# 학생 배치에 N^2
# 각 학생마다 돌면서 다시 자리배치를 하므로 N^2 * N^2 라 N^4이지만
# 자리를 앉힌 경우 제외하므로 최악의 경우에도 N^2
# 만족도 계산시 모든 자리 다시 탐색하므로 O(N^2)

# O(N^2) + O(N^2) = O(2N^2) ~= O(N^2)
# 문제에서 주어진 최대 크기(N ≤ 20)일 경우, 최악의 경우 400번 연산이므로 충분히 가능
