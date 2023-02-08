import sys

cnt = int(sys.stdin.readline())

for _ in range(cnt):
    n = int(sys.stdin.readline())
    li = list(map(int, sys.stdin.readline().split()))

    result = 0
    max_ = 0
    for i in range(len(li)-1, -1, -1):
        if li[i] > max_:
            max_ = li[i]
        else:
            result += max_ - li[i]

    print(result)




# 시간 초과
    # hold = []
    # for i in range(n):
    #     if li[i] != max(li):
    #         hold.append(li[i])
    #     else:
    #         result += len(hold) * li[i] - sum(hold)
    #         hold = []
    #     li[i] = 0
    #
    # print(result)
