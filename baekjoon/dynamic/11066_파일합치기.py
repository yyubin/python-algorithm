import sys
t = int(sys.stdin.readline())

for _ in range(t):
    k = int(sys.stdin.readline())
    li = [0] + list(map(int, sys.stdin.readline().split()))

    d = [[0 for _ in range(k+1)] for _ in range(k+1)]
    s = [0 for _ in range(k+1)]

    for i in range(1, k+1):
        s[i] = s[i-1] + li[i]

    for i in range(2, k+1):
        for j in range(1, k+2-i):
            d[j][i+j-1] = min([d[j][j+v] + d[j+v+1][j+i-1] for v in range(i-1)]) + s[j+i-1] - s[j-1]

    print(d[1][k])

# ex
# 파일길이가 3일경우
# (1 + 2,3) (1,2 +3), (2 + 3,4), (2,3 + 4) 일 수 있는데
# 1번부터 3번까지의 파일 비용은
# 1~1(O) + 2~3(60) 비용이 1~2(70) 3~3(0) 보다 적고
# 여기에 1~3의 누적합을 더해주면 된다. 그럼 d[1][3] = 160

#너무어려운데
#https://data-make.tistory.com/402