import sys
s1 = sys.stdin.readline().rstrip().upper()
s2 = sys.stdin.readline().rstrip().upper()

len1 = len(s1)
len2 = len(s2)
graph = [[0] * (len2+1) for _ in range(len1+1)]

for i in range(1, len1+1):
    for j in range(1, len2+1):
        if s1[i-1] == s2[j-1]:
            graph[i][j] = graph[i-1][j-1] + 1
        else:
            graph[i][j] = max(graph[i-1][j], graph[i][j-1])

print(graph[-1][-1])
