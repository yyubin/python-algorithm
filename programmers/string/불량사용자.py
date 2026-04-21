def solution(user_id, banned_id):
    d = dict()

    for banned in banned_id:
        if banned not in d:
            d[banned] = [1, []]
        else:
            d[banned][0] += 1

    print(d)
    s = set()
    for user in user_id:
        for banned in banned_id:
            if (user, banned) not in s:
                s.add((user, banned))
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
                d[banned][1].append(user)

    print(d)
    answer = 0

    tmp = []
    for key, data in d.items():
        if data[0] == len(data[1]):
            tmp.extend(data[1])
            continue



    return answer

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))