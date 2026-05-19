def solution(scores):
    wanho = scores[0]
    wanho_sum = sum(wanho)

    scores.sort(key=lambda x: (-x[0], x[1]))

    max_b = 0
    rank = 1

    for a, b in scores:
        if b < max_b:
            if [a, b] == wanho:
                return -1
            continue

        max_b = max(max_b, b)

        if a + b > wanho_sum:
            rank += 1

    return rank

#### 시간 초과
# def solution(scores):
#     w = scores[0]
#     scores.sort(key= lambda x: (-(x[0] + x[1]), -abs(x[0] - x[1])))
#
#     wi = scores.index(w)
#     incentive = [-1] * len(scores)
#     now = sum(scores[0])
#     i = 0
#     while i < wi + 1:
#         tmp = sum(scores[i])
#         if now == tmp:
#             incentive[i] = now
#             i += 1
#         else:
#             j = i - 1
#             while j > -1:
#                 if scores[j][0] > scores[i][0] and scores[j][1] > scores[i][1]:
#                     i += 1
#                     break
#                 j -= 1
#             else:
#                 incentive[i] = tmp
#                 i += 1
#
#     if incentive[wi] == -1:
#         return -1
#
#     ws = sum(w)
#     res = 1
#     for inc in incentive:
#         if inc == -1:
#             continue
#         if ws == inc:
#             break
#         res += 1
#     return res

print(solution([[2,2],[1,4],[3,2],[3,2],[2,1]]))
print(solution([[2, 2], [3, 3], [1, 10]]))