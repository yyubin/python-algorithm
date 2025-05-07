import sys
n = int(sys.stdin.readline())
n_li = [sys.stdin.readline().rstrip() for _ in range(n)]
m = int(sys.stdin.readline())
m_li = [sys.stdin.readline().rstrip() for _ in range(m)]
s = set()
pre_x, post_x = 0, 0
if n == 1 and n_li[0] == '?':
    print(m_li[0])
    sys.exit()

for i in range(n):
    s.add(n_li[i])
    if n_li[i] == "?":
        if i == 0:
            pre_x = -1
            post_x = n_li[i+1][0]
        elif i == n-1:
            pre_x = n_li[i-1][-1]
            post_x = -1
        else:
            pre_x = n_li[i-1][-1]
            post_x = n_li[i+1][0]

for i in range(m):
    now = m_li[i]
    flag = True
    if pre_x != -1:
        if now[0] != pre_x:
            flag = False
    if post_x != -1:
        if now[-1] != post_x:
            flag = False
    if now in s:
        flag = False
    if flag:
        print(now)
        break



