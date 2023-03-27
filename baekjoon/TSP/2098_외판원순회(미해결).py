import sys


def tsp(idx, path):
    if path == total:
        return graph[idx][0] if graph[idx][0] > 0 else 20202020
    if memo[idx][path] > 0:
        return memo[idx][path]

    tmp = 20202020
    for i in range(1, n):
        if (path >> i) % 2 == 1 or graph[idx][i] == 0:
            continue
        tmp = min(tmp, graph[idx][i] + tsp(i, path | (1 << i)))
    memo[idx][path] = tmp
    return tmp


n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
memo = [[0] * (1 << n) for _ in range(n)]
total = (1 << n) - 1
print(tsp(0, 1))

# dp 개새키
# 시간 초과...
# import sys
# n = int(sys.stdin.readline())
# INF = int(1e9)
# dp = [[INF] * (1 << n) for _ in range(n)]
#
# def dfs(x, visited):
#     if visited == (1 << n) - 1:
#         if graph[x][0]:
#             return graph[x][0]
#         else:
#             return INF
#
#     if dp[x][visited] != INF:
#         return dp[x][visited]
#
#     for i in range(1, n):
#         if not graph[x][i]:
#             continue
#         if visited & (1 << i):
#             continue
#
#         dp[x][visited] = min(dp[x][visited], dfs(i, visited | (1 << i)) + graph[x][i])
#     return dp[x][visited]
#
#
# graph = []
# for i in range(n):
#     graph.append(list(map(int, sys.stdin.readline().split())))
#
# print(dfs(0, 1))


## dp, dfs, bitmasking 문제
# 각 도시 방문 여부는 비트마스킹,
# 현재 도시에서의 최소비용은 dp
# 도시 방문은 dfs

# 출발 도시 지정
# 그래프는 순환경로(사이클)을 이룸
# 1 , 0, 3, 2, 1 이 최소비용이라면
# 0,3,2,1,0 도 최소비용

# 거쳐간 도시를 비트마스킹으로 표시
# 0001 이면 0번 도시만 거침
# 0011 이면 0, 1번 도시 거침
# 1111 이면 0, 1, 2, 3번 도시 거침

# dp에는 현재 도시에서 남은 도시들을 거쳐 다시 출발점으로 돌아오는 비용 저장
# dp[cur][visited] 는 현재 cur도시이고 방문현황은 visited에 있다
# 아직 방문하지 않은 도시들을 모두 거쳐 다시 시작점으로 가는데에 드는 최소 비용

# dp[next][nextvisited]일 경우 next도시에서 남은 도시들을 모두 거쳐 다시 시작적으로 가는 최소비용
# dp[cur][visited]는 dp[next][nextvisited]보다 graph[cur][next]만큼의 비용이 더 든다
# 다음 지점 dp보다 다음지점으로 가는 비용이 추가되는 것

# ex)
# dp[0][0011] = dp[0][3] 현재 0번 도시이고 0, 1번 도시 방문하였고
# 2, 3을 더 돈 후 다시 시작점으로 갈때의 최소비용
# dp[0][0011] = dp[2][0111] + graph[0][2] 이다

# 점화식
# dp[cur][visited] = min(dp[cur][visited], dp[next][visited | (1 << next)] + graph[cur][next])


# 비트마스킹
# https://velog.io/@1998yuki0331/Python-%EB%B9%84%ED%8A%B8-%EB%A7%88%EC%8A%A4%ED%82%B9-%EC%A0%95%EB%A6%AC
# 참조
# https://hongcoding.tistory.com/83
