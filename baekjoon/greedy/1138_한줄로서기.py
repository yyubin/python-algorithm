import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

result = [0] * n

for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt == li[i] and result[j] == 0:
            result[j] = i+1
            break

        if result[j] == 0:
            cnt += 1

print(*result)



# 4
# 2 1 1 0

# 4 2 1 3

# 0이 자기보다 키큰 사람이 왼쪽에 한명도 없었다.

# 1은 자기보다 키큰 사람이 왼쪽에 한명
# 3이 4에 서서 왼쪽을 봤을때 자기보다 키큰 사람 한명(4)

# 1은 자기보다 키큰 사람이 왼쪽에 한명
# 근데 3이 이미 4에 섰으니 그 앞으로 와야 하는데
# 맨 앞줄에 이미 4가 서있음
# 4가 남은 숫자(1,2)보다 큰데 1이 들어가면
# 키큰 사람이 2명이 됨
# 그래서 2번에 서고
