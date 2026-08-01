def solution(info, edges):
    answer = 0

    tree = [[] for _ in range(len(info))]
    for parent, child in edges:
        tree[parent].append(child)

    def dfs(current, sheep, wolf, next_nodes):
        nonlocal answer

        if info[current] == 0:
            sheep += 1
        else:
            wolf += 1

        if wolf >= sheep:
            return

        answer = max(answer, sheep)

        new_next_nodes = list(next_nodes)
        new_next_nodes.extend(tree[current])

        for next_node in new_next_nodes:
            send_nodes = [n for n in new_next_nodes if n != next_node]
            dfs(next_node, sheep, wolf, send_nodes)

    dfs(0, 0, 0, [])

    return answer

# def dfs(now, graph, info, wolves, wolf):
#     if info[now] == 0:
#         wolves[now] = wolf
#     else:
#         wolf += 1
#
#     for next in graph[now]:
#         dfs(next, graph, info, wolves, wolf)
#
#
# def solution(info, edges):
#     graph = [[] for _ in range(len(info))]
#
#     for edge in edges:
#         a, b = edge[0], edge[1]
#         graph[a].append(b)
#
#     print(graph)
#
#     wolves = [-1] * len(info)
#     dfs(0, graph, info, wolves, 0)
#
#     print(wolves)
#
#     sheep = wolves.count(0)
#     wolves = [i for i in wolves if i != -1 and i != 0]
#     wolves.sort(reverse=True)
#
#     print(wolves)
#
#     while wolves:
#         t = wolves.pop()
#         if t < sheep:
#             sheep += 1
#         else:
#             break
#
#     return sheep
#
#
print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
print(solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))