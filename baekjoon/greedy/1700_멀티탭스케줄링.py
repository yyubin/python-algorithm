import sys
from collections import defaultdict

n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

cnt = 0
multi_tap = []

while li:
    tmp = li.pop(0)

    if len(multi_tap) < n and tmp not in multi_tap:
        multi_tap.append(tmp)
        continue

    if tmp not in multi_tap:
        # 앞으로 사용 계획 없는 탭 빼기
        for i in multi_tap:
            flag = False
            for j in li:
                if j == i:
                    flag = True
            if not flag:
                multi_tap.remove(i)
                multi_tap.append(tmp)
                cnt += 1
                break
        else:
            dic = {}
            for i, v in enumerate(li):
                if v not in dic:
                    dic[v] = i
                dic[v] = min(dic[v], i)
            sort_li = sorted(dic.items(), key=lambda x: -x[1])

            # 사용 계획 있지만 우선순위가 낮은 것 빼기
            for i in sort_li:
                if i[0] in multi_tap:
                    multi_tap.remove(i[0])
                    multi_tap.append(tmp)
                    cnt += 1
                    break
print(cnt)

# 로직 개선 여지가 많을 것 같지만 자력솔이니 우선은 넘어감
