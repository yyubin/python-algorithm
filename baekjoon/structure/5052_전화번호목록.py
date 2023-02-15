import sys
tc = int(sys.stdin.readline())

for _ in range(tc):
    n = int(sys.stdin.readline())
    li = []
    for _ in range(n):
        li.append(sys.stdin.readline().rstrip())

    li.sort()

    for i in range(len(li) - 1):
        if li[i] in li[i+1][0:len(li[i])]: #정렬후 가능성이 높은 앞뒤 문자열만 비교
            print("NO")
            break
    else:
        print("YES")







# 시간초과
    # result = []
    # cnt = 0
    # for i in li:
    #     if cnt > 0:
    #         break
    #     stack = []
    #     tmp = list(i)
    #     for j in tmp:
    #         stack.append(j)
    #         if "".join(stack) in result:
    #             cnt += 1
    #             break
    #     result.append(i)
    # print("YES" if cnt == 0 else "NO")
