import sys
n = int(sys.stdin.readline())
li = []
dic = {}
for _ in range(n):
    team, num, score = map(int, sys.stdin.readline().split())
    li.append((team, num, score))
    if team not in dic:
        dic[team] = 0
li.sort(key=lambda x: -x[2])
cnt = 0
for i in li:
    if cnt > 2:
        sys.exit()
    if dic[i[0]] < 2:
        print(i[0], i[1])
        dic[i[0]] += 1
        cnt += 1
