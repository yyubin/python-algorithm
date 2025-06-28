import sys
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    words = [sys.stdin.readline().rstrip() for _ in range(n)]

    ans = 0
    for ch in 'abcde':
        tmp_li = []
        for w in words:
            c = w.count(ch)
            tmp_li.append(2*c - len(w))
        tmp_li.sort(reverse=True)

        cur, cnt = 0, 0
        for t in tmp_li:
            if cur + t > 0:
                cur += t
                cnt += 1
            else:
                break
        ans = max(ans, cnt)
    print(ans)

    # for target in ['a', 'b', 'c', 'd', 'e']:
    #     flag = True
    #     tmp_li = []
    #     for word in words:
    #         score = 0
    #         for l in word:
    #             if l == target:
    #                 score += 1
    #         tmp_li.append((2*score - len(word), word))
    #     tmp_li.sort(key=lambda x: (x[0]), reverse=True)
    #
    #     now = n
    #
    #     while now > 0 and flag:
    #         tmp_dic = defaultdict(int)
    #         tmp_len = 0
    #         for s1, word in tmp_li:
    #             for l in word:
    #                 tmp_dic[l] += 1
    #                 tmp_len += 1
    #
    #         if tmp_dic[target] > tmp_len/2:
    #             flag = False
    #             ans = max(ans, now)
    #         else:
    #             now -= 1
    #             tmp_li.pop()
    #
    # print(ans)
    #

