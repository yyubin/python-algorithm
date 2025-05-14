import sys
from itertools import combinations
st = sys.stdin.readline().rstrip()
n = [x for x in range(1, len(st))]
ans = []
for x, y in combinations(n, 2):
    s1 = st[:x][::-1]
    s2 = st[x:y][::-1]
    s3 = st[y:][::-1]
    ans.append(''.join(s1+s2+s3))

ans.sort()
print(ans[0])

# 그리디하게는 어려운듯..
# import sys
# string = sys.stdin.readline().rstrip()
# cnt = 0
# res = ''
# while cnt < 3:
#     if cnt == 2:
#         min_ = min(string)
#     else:
#         min_ = min(string[:len(string) - (2-cnt)])
#     cnt += 1
#     idx = string.index(min_)
#
#     tmp = ''
#     for i in range(idx+1):
#         tmp += string[i]
#     string = string[idx+1:]
#     res += tmp[::-1]
# print(res)