import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
now = 1
score = [1]
for i in range(n-2, -1, -1):
    if now < li[i]:
        now += 1
        score.append(now)
    else:
        now = li[i]
        score.append(now)
print(sum(score))


# 감속 조건이 엄격(1씩만 가능)할 때 → 뒤에서부터 역으로 접근해야 할 가능성이 높다.
# "이전 상태가 다음 상태에 제약을 받는다" → 뒤에서부터 greedy나 DP를 떠올리기