## 최단경로면 다익스트라인데
# 음수 가중치가 있어서 벨만-포드 알고리즘 따로 공부해서 풀이함..
# 다익스트라는 음수 가중치는 적용x
# 다익스트라보단 성능 떨어짐

# 출발지와 도착지가 같은 웜홀이 있을 경우 바로 yes
# 음수사이클있을 경우 yes
# 1번만 bf 돌려도 모든 지점에서의 음수 사이클 확인 가능


def bf(start):
    distance[start] = 0

    for i in range(n):
        for cur in range(n+1):
            for next, cost in edges[cur]:
                if distance[cur] + cost < distance[next]:
                    if i == n-1:
                        return "YES"
                    distance[next] = distance[cur] + cost

    return "NO"



import sys
for _ in range(int(sys.stdin.readline())):
    n, m, w = map(int, sys.stdin.readline().split())
    edges = [[] for _ in range(n+1)]


    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        edges[a].append((b, c))
        edges[b].append((a, c))

    w_flag = False
    for _ in range(w):
        a, b, c = map(int, sys.stdin.readline().split())
        if a == b:
            w_flag = True

        edges[a].append((b, c*-1))

    if w_flag:
        print("YES")
        continue


    distance = [sys.maxsize] * (n + 1)

    print(bf(1))



