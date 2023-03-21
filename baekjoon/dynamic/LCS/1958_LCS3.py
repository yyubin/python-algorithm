import sys

s1 = sys.stdin.readline().rstrip()
s2 = sys.stdin.readline().rstrip()
s3 = sys.stdin.readline().rstrip()

len1 = len(s1)
len2 = len(s2)
len3 = len(s3)
graph = [[[0]*(len(s3)+1) for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]

for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        for k in range(1, len3 + 1):
            if s1[i-1] == s2[j-1] == s3[k-1]:
                graph[i][j][k] = graph[i-1][j-1][k-1] + 1
            else:
                graph[i][j][k] = max(graph[i-1][j][k], graph[i][j-1][k], graph[i][j][k-1])

print(graph[-1][-1][-1])
