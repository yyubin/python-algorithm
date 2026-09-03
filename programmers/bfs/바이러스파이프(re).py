from collections import deque


def solution(n, infection, edges, k):
    graph = [[] for _ in range(n + 1)]
    edge_types = set()

    for x, y, edge_type in edges:
        graph[x].append((y, edge_type))
        graph[y].append((x, edge_type))
        edge_types.add(edge_type)

    def spread(infected, selected_type):
        q = deque()

        for node in range(1, n + 1):
            if infected & (1 << node):
                q.append(node)

        next_infected = infected

        while q:
            now = q.popleft()

            for nxt, edge_type in graph[now]:
                if edge_type != selected_type:
                    continue

                if next_infected & (1 << nxt):
                    continue

                next_infected |= 1 << nxt
                q.append(nxt)

        return next_infected

    start = 1 << infection

    q = deque([(start, 0, None)])

    visited = {(start, 0, None)}

    answer = 1

    while q:
        infected, times, prev = q.popleft()

        if times == k:
            answer = max(answer, bin(infected).count("1"))
            continue

        for edge_type in edge_types:
            if edge_type == prev:
                continue

            next_infected = spread(infected, edge_type)

            if next_infected == infected:
                continue

            state = (
                next_infected,
                times + 1,
                edge_type
            )

            if state in visited:
                continue

            visited.add(state)
            q.append(state)

    return answer


print(
    solution(
        10,
        1,
        [
            [1, 2, 1],
            [1, 3, 1],
            [1, 4, 3],
            [1, 5, 2],
            [5, 6, 1],
            [5, 7, 1],
            [2, 8, 3],
            [2, 9, 2],
            [9, 10, 1]
        ],
        2
    )
)

print(
    solution(
        7,
        6,
        [
            [1, 2, 3],
            [1, 4, 3],
            [4, 5, 1],
            [5, 6, 1],
            [3, 6, 2],
            [3, 7, 2]
        ],
        3
    )
)