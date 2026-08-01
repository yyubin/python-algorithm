from collections import defaultdict

def solution(id_list, report, k):
    d = defaultdict(set)

    for r in report:
        from_, to_ = r.split()
        d[to_].add(from_)

    res = defaultdict(int)
    for i, id in enumerate(id_list):
        if len(d[id]) >= k:
            for t in d[id]:
                res[t] += 1

    answer = [res[id] for id in id_list]
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))