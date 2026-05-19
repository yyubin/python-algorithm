# 마지막에 점수로 접근해서 비교하는 것도 줄여야 통과
# 해당 부분은 이분탐색
# 쓸데없이 해싱 빼고 문자열 그대로 ㄱㄱ


from collections import defaultdict
from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    dic = defaultdict(list)

    for v in info:
        tmp = v.split()
        score = int(tmp.pop())

        for r in range(5):
            for comb in combinations(range(4), r):
                condition = tmp[:]

                for idx in comb:
                    condition[idx] = "-"

                key = tuple(condition)
                dic[key].append(score)

    for key in dic:
        dic[key].sort()

    answer = []

    for q in query:
        q = q.replace(" and ", " ")
        tmp = q.split()
        score = int(tmp.pop())

        key = tuple(tmp)
        scores = dic[key]

        idx = bisect_left(scores, score)
        answer.append(len(scores) - idx)

    return answer

# from collections import defaultdict
# def solution(info, query):
#     dic = defaultdict(list)
#     scores = []
#     for i, v in enumerate(info):
#         tmp = v.split()
#         scores.append(int(tmp.pop()))
#
#         tmpl = [tmp]
#         tmpl.append(["-", tmp[1], tmp[2], tmp[3]])
#         tmpl.append([tmp[0], "-", tmp[2], tmp[3]])
#         tmpl.append([tmp[0], tmp[1], "-", tmp[3]])
#         tmpl.append([tmp[0], tmp[1], tmp[2], "-"])
#
#         tmpl.append(["-", "-", tmp[2], tmp[3]])
#         tmpl.append(["-", tmp[1], "-", tmp[3]])
#         tmpl.append([tmp[0], "-", "-", tmp[3]])
#         tmpl.append(["-", tmp[1], tmp[2], "-"])
#         tmpl.append([tmp[0], tmp[1], "-", "-"])
#         tmpl.append([tmp[0], "-", tmp[2], "-"])
#
#         tmpl.append(["-", "-", "-", tmp[3]])
#         tmpl.append([tmp[0], "-", "-", "-"])
#         tmpl.append(["-", "-", tmp[2], "-"])
#         tmpl.append(["-", tmp[1], "-", "-"])
#
#         tmpl.append(["-", "-", "-", "-"])
#
#         for k in tmpl:
#             dic[hash("".join(k))].append(i)
#
#     answer = []
#     for i, q in enumerate(query):
#         qq = q.replace("and", "")
#         tmp = qq.split()
#         score = int(tmp.pop())
#
#         cnt = 0
#         for v in dic[hash("".join(tmp))]:
#             if scores[v] >= score:
#                 cnt += 1
#
#         answer.append(cnt)
#
#     return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))

# def solution(info, query):
#     java, python, cpp, backend, frontend, junior, senior, pizza, chicken = set(), set(), set(), set(), set(), set(), set(), set(), set()
#     dic = {"java": java, "python": python, "cpp": cpp, "backend": backend, "frontend": frontend, "junior": junior, "senior": senior, "pizza": pizza, "chicken": chicken}
#
#     scores = []
#     for i, v in enumerate(info):
#         lang, tech, hist, food, score = v.split()
#         dic[lang].add(i)
#         dic[tech].add(i)
#         dic[hist].add(i)
#         dic[food].add(i)
#         scores.append(int(score))
#
#
#     answer = []
#     for i, q in enumerate(query):
#         li = q.split("and")
#         fd, sc = li.pop().split()
#         li.append(fd)
#
#         can = set([i for i in range(len(info))])
#         for j in li:
#             tmp = j.strip()
#             if tmp in dic:
#                 can &= set(dic[tmp])
#
#         cnt = 0
#         for j in can:
#             if scores[j] >= int(sc):
#                 cnt += 1
#         answer.append(cnt)
#     return answer
#
# print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
# 쿼리에서 100,000 * 50,000 이라 시간 초과