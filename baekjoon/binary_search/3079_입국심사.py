import sys
n, m = map(int, sys.stdin.readline().split())
li = []

for _ in range(n):
    li.append(int(sys.stdin.readline().strip()))

start = 1
end = m * max(li)

result = 1000000000000000000

while start <= end:
    mid = (start + end) // 2
    total = sum(mid // i for i in li)

    if total < m:
        start = mid + 1
    else:
        result = min(result, mid)
        end = mid - 1

print(result)


# 심사대의 상태나 사람의 명수가 어떻든 '결국에 최소로 진행될 수 있는 시간' Tans 가 있다고 하겠습니다.
#
# 그러면 이 T가 존재할 수 있는 범위에 대해서 먼저 생각해보면
#
#
#
# 제일 시간이 오래걸리는 심사대에서 걸리는 시간 Tmax 에 사람 수 N을 곱한 값이 될 것입니다. N명이 모두 Tmax에서만 심사를 받는 경우에요.
#
# 최소는 대충 1이라고 잡아도 되겠습니다. Tk의 범위는 1이상이니까요
#
#
# 그러면 이제 어떤 시간 Tk 를 정해놓겠습니다.
#
# 그리고 Tk초 안에 모든 사람이 심사대에 통과할 수 있는지 알아봅니다.
#
# 모든 사람이 Tk초 안에 심사대를 통과할 수 있으면 Tk가 Tans가 될 수도있고, 아니면 더 적은시간에도 가능할 수도 있겠죠.
#
# 반대로 모든 사람이 Tk초 안에 심사대를 통과할 수 없으면 Tk는 정답이 될 수 없습니다. 더 많은 시간이 필요하죠.
#
# 그러면 이제 모든 사람이 Tk초 안에 심사대를 통과할 수 있는지 없는지를 알아봐야합니다.
#
# 모든 사람이 Tk초 안에 통과할 수 있으려면 '각 심사대에서 Tk초 동안 통과시킬 수 있는 사람 수'를 각각 구해서 더해보고 그게 N명 이상이면 가능하다는 뜻입니다.
#
# 그래서 count += mid//time 을 하는 것입니다.
# Tk로 Tans를 찾아내는 과정을 이분탐색으로 진행할 수 있습니다