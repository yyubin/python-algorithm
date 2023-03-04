import sys
s = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()
d = [[0] * len(t) for _ in range(len(s))]
result = 0

for i in range(len(s)):
    for j in range(len(t)):
        if s[i] == t[j]: #두 문자열이 같을 경우
            if i == 0 or j == 0:
                d[i][j] = 1
            else:
                d[i][j] = d[i-1][j-1] + 1 #전문자열보다 1증가
            result = max(result, d[i][j])

print(result)

#https://lmcoa15.tistory.com/73
#dp따로 공부해야할둣..