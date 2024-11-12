import sys
s = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline())
a = [sys.stdin.readline().rstrip() for _ in range(n)]
a.sort(key=len, reverse=True)

d = [False] * (len(s)+1)
d[0] = True

for i in range(len(s)+1):
    if d[i]:
        for j in a:
            if s[i:i+len(j)] == j:
                d[i+len(j)] = True

print(1 if d[-1] else 0)


# string + dp
# dp배열에 해당 인덱스까지 a에 포함된 문자열로 표현 가능한지 체크
# softwarecontest
# 2
# software
# contest
# 의 경우 처음 software는 softwarecontenst의 0번부터 6번 인덱스까지를 표현, 가능하므로 7에 True
# 시작 가능한 위치를 지정하므로 문자열 만큼 for(첫번째)를 순회하고
# 내부에 단어가 있으면 시작 가능위치를 다시 표시하는 메모이제이션
# https://squareyun.tistory.com/114/

# 긴 문자열부터 검사하는게 조금 더 빠름