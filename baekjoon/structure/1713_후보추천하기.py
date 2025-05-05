import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
dic = {i: 0 for i in range(1, m + 1)}
res = []
for i in li:
    if i in res:
        dic[i] += 1
        continue

    if len(res) < n:
        res.append(i)
        dic[i] += 1
    else:
        min_ = []
        min_val = sys.maxsize
        for j in res:
            if dic[j] < min_val:
                min_val = dic[j]
                min_ = [j]
            elif dic[j] == min_val:
                min_.append(j)

        tmp = min_[0]
        res.remove(tmp)
        dic[tmp] = 0
        res.append(i)
        dic[i] += 1

res.sort()
print(*res)
