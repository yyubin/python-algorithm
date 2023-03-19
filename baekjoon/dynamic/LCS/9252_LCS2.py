import sys
s1 = sys.stdin.readline().rstrip().upper()
s2 = sys.stdin.readline().rstrip().upper()

len1 = len(s1)
len2 = len(s2)
graph = [[""] * (len2+1) for _ in range(len1+1)]
result = []

for i in range(1, len1+1):
    for j in range(1, len2+1):
        if s1[i-1] == s2[j-1]:
            graph[i][j] = graph[i-1][j-1] + s1[i-1]
        else:
            if len(graph[i-1][j]) >= len(graph[i][j-1]):
                graph[i][j] = graph[i-1][j]
            else:
                graph[i][j] = graph[i][j-1]

print(len(graph[-1][-1]), graph[-1][-1], sep="\n")
