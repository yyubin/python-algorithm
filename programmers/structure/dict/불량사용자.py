from itertools import permutations
from collections import defaultdict

def solution(user_id, banned_id):
    d = defaultdict(list)

    visited = set()
    for user in user_id:
        for banned in banned_id:
            if (user, banned) not in visited:
                visited.add((user, banned))
            else:
                continue

            if len(banned) != len(user):
                continue
            tmp = 0
            for i in range(len(banned)):
                if banned[i] == "*":
                    tmp += 1
                    continue
                if banned[i] == user[i]:
                    tmp += 1
                else:
                    break

            if tmp == len(banned):
                d[banned].append(user)

    s = set()
    for per in permutations(user_id, len(banned_id)):
        for i, p in enumerate(per):
            if p not in d[banned_id[i]]:
                break
        else:
            tu = tuple(sorted(per))
            if tu not in s:
                s.add(tu)

    return len(s)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))

# 2개에서 겹친 경우 -1
# 3개에서 겹친 경우 -4
# 4개에서 겹친 경우 -9