from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    orders = [sorted(list(i)) for i in orders]
    counter = defaultdict(int)

    course_map = defaultdict(int)

    for order in orders:
        for c in course:
            for com in combinations(order, c):
                counter[com] += 1

                if course_map[c] < counter[com]:
                    course_map[c] = counter[com]

    answer = []
    for val, count in counter.items():
        l = len(val)
        if course_map[l] > 1 and course_map[l] == count:
            answer.append(''.join(val))
    answer.sort()
    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))