# def ice_count(li3:list):
#     count = 0
#     for v in li3:
#         # [0, 0] 확인시 [1,0] [0,1]이 근접해 있는데 둘다 확인해야함
#         # x축 먼저 확인하면서 연결 되어있는지 우선 확인,
#         # 단, 앞서 확인한 라인과 같은 곳이면 카운트 X
#         # 00110의 경우 2번 확인하지만
#         # 다음 라인인 00011의 경우 라인이 겹치는 부분이 발생하기 때문에 카운트 하지 않는다
#         pass
#         if v == 0:
#             # if i != 0 and li[i-1] != 0:
#             #     count += 1
#             # if i == 0 and v == 0:
#                 count += 1
#         print(count)
#
#
# n, m = map(int, input().split())
# li = []
# for i in range(n):
#     li2 = list(map(int, input()))
#     li.append(li2)
#
# for i in range(n):
#     li3 = li[i]
#     ice_count(li3)

# def icecream():
#     n, m = map(int, input().split())
#     graph = []
#     for i in range(n):
#         graph.append(list(map(int, input())))
#
#     def count_ice(x, y):
#         if x <= -1 or x >= n or y <= -1 or y >= m:
#             return False
#         if graph[x][y] == 0:
#             print("확인하는 값", x, y)
#             graph[x][y] = 1
#             count_ice(x - 1, y)  # 서
#             count_ice(x, y - 1)  # 남
#             count_ice(x + 1, y)  # 동
#             count_ice(x, y + 1)  # 북
#             return True
#         return False
#
#     result = 0
#     for i in range(n):
#         for j in range(m):
#             if count_ice(i, j) == True:
#                 result += 1
#
#     print(result)



n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def map(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0

        if graph[x + 1][y] == 1 or graph[x][y - 1] == 1:
            map(x + 1, y)
            map(x, y - 1)
        else:
            map(x - 1, y)  # 서
            map(x, y - 1)  # 남
            map(x + 1, y)  # 동
            map(x, y + 1)  # 북

        return True

result = 0
for i in range(n):
    for j in range(m):
        if map(i, j) == True:
            result += 1

print(result)


