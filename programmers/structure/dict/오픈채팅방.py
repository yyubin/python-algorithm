from collections import defaultdict
def solution(record):
    users = defaultdict(str)
    for r in record:
        li = r.split()
        if li[0] == "Enter" or li[0] == "Change":
            users[li[1]] = li[2]

    answer = []
    for r in record:
        li = r.split()
        if li[0] == "Enter":
            answer.append(f"{users[li[1]]}님이 들어왔습니다.")
        elif li[0] == "Leave":
            answer.append(f"{users[li[1]]}님이 나갔습니다.")

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))