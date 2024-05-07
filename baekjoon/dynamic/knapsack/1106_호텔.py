import sys
c, n = map(int, sys.stdin.readline().split())
city = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
city.sort()
d = [0] + [sys.maxsize] * (c+100)
result = sys.maxsize

for w, v in city:
    for i in range(v, len(d)):
        d[i] = min(d[i-v]+w, d[i])
        if i >= c:
            result = min(d[i], result)

print(result)


### https://seokhee0516.tistory.com/5