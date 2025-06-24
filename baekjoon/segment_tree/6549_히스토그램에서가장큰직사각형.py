import sys
while True:
    li = list(map(int, sys.stdin.readline().split()))
    if li[0] == 0:
        break
    li.append(0)

    ret = 0
    stack = [[0, 0]]
    for i in range(1, li[0]+2):
        while stack[-1][1] > li[i]:
            tmp = stack.pop()
            tmp_a = 0
            while stack[-1][1] == tmp[1]:
                stack.pop()
            tmp_a = max((i-1-stack[-1][0]) * tmp[1], (i-tmp[0]) * tmp[1])

            if tmp_a > ret:
                ret = tmp_a

        stack.append([i, li[i]])
    print(ret)

