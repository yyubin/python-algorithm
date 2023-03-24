import sys
n = int(sys.stdin.readline())

li = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    li.append((a, b))

li.append(li[0])

result1 = 0
result2 = 0
for i in range(n):
    result1 += li[i][0] * li[i+1][1]
    result2 += li[i][1] * li[i+1][0]

print(round(abs((result1-result2)/2), 1))

#좌표값으로 다각형 넓이 구하기
#https://ko.wikihow.com/%EB%8B%A4%EA%B0%81%ED%98%95-%EB%84%93%EC%9D%B4-%EA%B5%AC%ED%95%98%EA%B8%B0#:~:text=%EC%A0%95%EB%8B%A4%EA%B0%81%ED%98%95%EC%9D%98%20%EB%84%93%EC%9D%B4%EB%A5%BC%20%EA%B5%AC,%EC%9D%98%20%EC%A4%91%EC%8B%AC%EC%9C%BC%EB%A1%9C%20%EB%AA%A8%EC%9D%B4%EB%8A%94%20%EC%84%A0%EB%B6%84

