import sys
n, m, r = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
r_li = list(map(int, sys.stdin.readline().split()))

def op1():
    global graph
    graph = graph[::-1]
    return graph

def op2():
    global graph
    temp = [[0] * m for _ in range(n)]
    for i in range(n):
        temp[i] = graph[i][::-1]
    return temp

def op3():
    global graph, n, m
    temp = list(map(list, zip(*graph[::-1])))
    n, m = m, n
    return temp

def op4():
    global graph, n, m
    temp = list(map(list, zip(*graph)))[::-1]
    n, m = m, n
    return temp

def op5():
    global graph, n, m
    temp = [[0] * m for _ in range(n)]
    idx_x = n//2
    idx_y = m//2

    for i in range(idx_x):
        for j in range(idx_y):
            temp[i][j] = graph[idx_x+i][j]

    for i in range(idx_x):
        for j in range(idx_y):
            temp[i][j+idx_y] = graph[i][j]

    for i in range(idx_x):
        for j in range(idx_y):
            temp[i+idx_x][j] = graph[i+idx_x][j+idx_y]

    for i in range(idx_x):
        for j in range(idx_y):
            temp[i+idx_x][j+idx_y] = graph[i][j+idx_y]

    return temp

def op6():
    global graph, n, m
    temp = [[0] * m for _ in range(n)]
    idx_x = n//2
    idx_y = m//2

    for i in range(idx_x):
        for j in range(idx_y):
            temp[i][j] = graph[i][idx_y+j]

    for i in range(idx_x):
        for j in range(idx_y):
            temp[i][j+idx_y] = graph[i+idx_x][j+idx_y]

    for i in range(idx_x):
        for j in range(idx_y):
            temp[i+idx_x][j] = graph[i][j]

    for i in range(idx_x):
        for j in range(idx_y):
            temp[i+idx_x][j+idx_y] = graph[i+idx_x][j]

    return temp

for i in range(r):
    if r_li[i] == 1:
        graph = op1()
    elif r_li[i] == 2:
        graph = op2()
    elif r_li[i] == 3:
        graph = op3()
    elif r_li[i] == 4:
        graph = op4()
    elif r_li[i] == 5:
        graph = op5()
    else:
        graph = op6()

for i in graph:
    print(*i)

# 시간복잡도 O(r*n*m)
