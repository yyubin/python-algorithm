# 음료수 얼려 먹기

# n, m = map(int, input().split())
# li = []
#
# for i in range(n):
#     li.append(list(map(int, input())))
#
#
# def check_ice(x: int, y: int):
#     # x는 0일때만 들어옴
#     # x는 방문처리하고
#     # x에서 오른쪽이 0이면 오른쪽으로 이동..?
#     # 오른쪽이 1이면 아래로 이동
#     # 둘다 0이면 종료
#     # 왼쪽이 0일 경우도 있음
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False
#
#     if li[x][y] == 0:
#         li[x][y] = 1
#         check_ice(x, y - 1)
#         check_ice(x - 1, y)
#         check_ice(x + 1, y)
#         check_ice(x, y + 1)
#         return True
#     return False
#
#
# result = 0
# print(li)
#
# for i in range(n):
#     for j in range(m):
#         if check_ice(i, j) == True:
#             result += 1
#
# print(result)


# 미로 탈출 문제
from collections import deque

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

def bfs(x:int, y:int):
    if x == n and y == m:
        return
    if graph[x][y] == 1:
        graph[x][y] = 0
        
