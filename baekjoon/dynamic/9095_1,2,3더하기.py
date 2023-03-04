import sys
t = int(sys.stdin.readline())

def sol(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return sol(n-1) + sol(n-2) + sol(n-3)


for _ in range(t):
    n = int(sys.stdin.readline())
    print(sol(n))







# 생각을 못해내 왜?!??!?!?!?
    # ans = 1
    # while True:
    #     if d[0] + 1 not in [1, 2, 3]:
    #         break
    #     d.pop(0)
    #     d[-1] += 1
    #     if sum(d) == n:
    #         ans += len(d)
    #
    # print(ans)

