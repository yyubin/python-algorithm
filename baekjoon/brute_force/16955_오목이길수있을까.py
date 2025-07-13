import sys
graph = [list(sys.stdin.readline().rstrip()) for _ in range(10)]

for i in range(10):
    for j in range(10):
        if i <= 5:
            col = []
            for k in range(5):
                col.append(graph[i+k][j])
            if col.count('X') == 4 and col.count('.') == 1:
                print(1)
                sys.exit()
        if j <= 5:
            row = []
            for k in range(5):
                row.append(graph[i][j+k])
            if row.count('X') == 4 and row.count('.') == 1:
                print(1)
                sys.exit()
        if i <= 5 and j <= 5:
            dia = []
            for k in range(5):
                dia.append(graph[i+k][j+k])
            if dia.count('X') == 4 and dia.count('.') == 1:
                print(1)
                sys.exit()
        if i >= 4 and j <= 5:
            rev = []
            for k in range(5):
                rev.append(graph[i-k][j+k])
            if rev.count('X') == 4 and rev.count('.') == 1:
                print(1)
                sys.exit()
print(0)