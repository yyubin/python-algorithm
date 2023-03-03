import sys
s = sys.stdin.readline().rstrip().split('-')
# 처음에 - 로 나눠서 받기
num = []

for i in s: #s에는 더해야하는 각각의 수만 남음
    cnt = 0
    s = i.split('+') # +기준으로 쪼개서 num에 넣어주고
    for j in s:
        cnt += int(j)
    num.append(cnt)

n = num[0]
for i in range(1, len(num)): # 처음 값에서 나머지 값들 다 빼주기
    n -= num[i]
print(n)
