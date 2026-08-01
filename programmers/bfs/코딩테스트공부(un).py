from collections import deque

def solution(alp, cop, problems):
    max_alp = max(x[0] for x in problems)
    max_cop = max(x[1] for x in problems)

    q = deque()
    q.append((alp, cop, 0))

    res = 1e9

    while q:
        now_alp, now_cop, cnt = q.popleft()

        if now_alp >= max_alp and now_cop >= max_cop:
            res = min(res, cnt)
            continue

        for problem in problems:
            if now_alp >= problem[0] and now_cop >= problem[1]:
                q.append((problem[2] + now_alp, problem[3] + now_cop, cnt + problem[4]))
            else:
                time = 0
                time += max(0, problem[0] - now_alp)
                time += max(0, problem[1] - now_cop)
                q.append((max(problem[0], now_alp) + problem[2], max(problem[1], now_cop) + problem[3], time + cnt + problem[4]))

    return res


print(solution(10, 10, [[10,15,2,1,2],[20,20,3,3,4]]))
print(solution(0, 0,  	[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]))


### 2차원 DP로 수정해야함